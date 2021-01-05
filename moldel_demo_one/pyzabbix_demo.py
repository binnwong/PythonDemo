from pyzabbix import ZabbixAPI


# 安装zabbix server的服务器ip
ZABBIX_SERVER = 'http://10.1.1.0/zabbix'

zapi = ZabbixAPI(ZABBIX_SERVER)
zapi.login('Admin', 'zabbix')


# 获取主机
host_list = zapi.host.get(
    output="extend",
)

# 获取触发器
triggers = zapi.trigger.get(
    output="extend",
    selectHosts=['host'],
)

# 获取应用
application_list = zapi.application.get(
    hostids='',
    output="extend",
)

# 获取监控项
item_list = zapi.item.get(
    hostids='',
    applicationids='',
    output="extend",
)

# 获取模板
template = zapi.template.get(
    output="extend",
)

# 通过key来帅选数据
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
