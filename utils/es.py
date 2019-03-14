# -*- coding: utf-8 -*-
# from elasticsearch import Elasticsearch
#from es_client import es_client
import time,datetime
import requests
import json

url = "http://es-monitor.hupu.io/accesslog-*/_search"

end = int(time.strftime("%s", time.localtime())) * 1000
t = time.localtime(time.time() - 10)
#10秒前
begin = int(time.strftime("%s", t)) * 1000

def post_qps(key):
    data = {
            "size": 0,
            "query": {
                "bool": {
                    "filter": [{
                        "range": {
                            "time": {
                                "gte": begin,
                                "lte": end,
                                "format": "epoch_millis"
                            }
                        }
                    },
                    {
                        "query_string": {
                            "query": key
                        }
                    }]
                }
            },
            "aggs": {
                "2": {
                    "date_histogram": {
                        "interval": "1s",
                        "field": "time",
                        "min_doc_count": 0,
                        "extended_bounds": {
                            "min": begin,
                            "max": end
                        },
                        "format": "epoch_millis"
                    },
                    "aggs": {}
                }
            }
        }
    print(json.dumps(data))
    try:
        r = requests.post(url,data=json.dumps(data))
    except:
        return "error"
    if r:
        a = json.loads(r.text)
        b = []
        for i in a["aggregations"]["2"]["buckets"]:
            b.append(i['doc_count'])
        b.sort(reverse=True)
        return b[0]

def post_rt(key):
    data = {
              "size": 0,
              "query": {
                "bool": {
                  "filter": [{
                    "range": {
                      "time": {
                        "gte": begin,
                        "lte": end,
                        "format": "epoch_millis"
                      }
                    }
                  }, {
                    "query_string": {
                      "query": key
                    }
                  }]
                }
              },
              "aggs": {
                "2": {
                  "date_histogram": {
                    "interval": "1s",
                    "field": "time",
                    "min_doc_count": 0,
                    "extended_bounds": {
                      "min": begin,
                      "max": end
                    },
                    "format": "epoch_millis"
                  },
                  "aggs": {
                    "1": {
                      "percentiles": {
                        "field": "request_time",
                        "percents": [99]
                      }
                    }
                  }
                }
              }
            }

    try:
        r = requests.post(url,data=json.dumps(data))
    except:
        return "error"
    if r:
        a = json.loads(r.text)
        b = []
        for i in a["aggregations"]["2"]["buckets"]:
            b.append(i["1"]["values"]["99.0"])

        b = list(set(b))
        if "NaN" in b:
            b.remove("NaN")
        # for index,value in enumerate(b):
        #     if value == "NaN":
        #         del(b[index])
        if len(b) == 0:
            return 0
        else:
            b.sort(reverse=True)
            c = float(b[0] * 1000)
            return float('%.2f' % c)