import json
import simplejson


list_json = [{'a': 'bbb'}, {'c': 'd: "d "d'}, {'e': 'fff'}]
print(type(list_json))
json_str = json.dumps(list_json, ensure_ascii=False)
print(json_str)
print(type(json_str))
simplejson_str = simplejson.dumps(list_json, ensure_ascii=False)
print(simplejson_str)
print(type(simplejson_str))

# print(json_str.replace('\\', ''))
# print(type(json_str.replace('\\', '')))

json_list = json.loads(json_str, encoding='utf-8', strict=False)
print(json_list)
# print(type(json_list))
# simplejson_list = simplejson.loads(simplejson_str, encoding='utf-8', strict=False)
# print(simplejson_list)
# print(type(simplejson_list))
