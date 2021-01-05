from pyzabbix import ZabbixAPI


# ��װzabbix server�ķ�����ip
ZABBIX_SERVER = 'http://10.1.1.0/zabbix'

zapi = ZabbixAPI(ZABBIX_SERVER)
zapi.login('Admin', 'zabbix')


# ��ȡ����
host_list = zapi.host.get(
    output="extend",
)

# ��ȡ������
triggers = zapi.trigger.get(
    output="extend",
    selectHosts=['host'],
)

# ��ȡӦ��
application_list = zapi.application.get(
    hostids='',
    output="extend",
)

# ��ȡ�����
item_list = zapi.item.get(
    hostids='',
    applicationids='',
    output="extend",
)

# ��ȡģ��
template = zapi.template.get(
    output="extend",
)

# ͨ��key��˧ѡ����
item_list = zapi.item.get(
    hostids='',
    search={
        "key_": '',
    },
    output="extend",
)


from pyzabbix.sender import ZabbixMetric, ZabbixSender

packet = [
  ZabbixMetric('hostname', 'test[system_status]', "OK"),
]

result = ZabbixSender(zabbix_server='zabbix_host', zabbix_port=10051).send(packet)
