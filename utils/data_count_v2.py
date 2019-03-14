# -*- coding: utf-8 -*-

import json


def connv2(v):
    for key,value in v.items():
        if key == "all":
            all = value

        if key == "all-api":
            all_api_all_api = []
            all_api_all = []
            all_api_sum = 0
            for i,j in value.items():
                b = j.split(',')[0]
                a = (i + ':' + '\n')
                all_api_sum = int(b) + int(all_api_sum)
                all_api_all.append(j)
                all_api_all_api.append(a)
            all_api_sum = all_api_sum
            all_api = (''.join(all_api_all))
            all_api_api = (''.join(all_api_all_api))

        if key == "reply-api":
            reply_api_all_api = []
            reply_api_all = []
            reply_api_sum = 0
            for i,j in value.items():
                b = j.split(',')[0]
                a = (i + ':' + '\n')
                reply_api_sum = int(b) + int(reply_api_sum)
                reply_api_all.append(j)
                reply_api_all_api.append(a)
            reply_api_sum = reply_api_sum
            reply_api = (''.join(reply_api_all))
            reply_api_api = (''.join(reply_api_all_api))

        if key == "thread-api":
            thread_api_all_api = []
            thread_api_all = []
            thread_api_sum = 0
            for i,j in value.items():
                b = j.split(',')[0]
                a = (i + ':' + '\n')
                thread_api_sum = int(b) + int(thread_api_sum)
                thread_api_all.append(j)
                thread_api_all_api.append(a)
            thread_api = (''.join(thread_api_all))
            thread_api_api = (''.join(thread_api_all_api))
            ss = thread_api_sum

    all_zuul = thread_api_sum + reply_api_sum + all_api_sum

    data = {
          "nodes": [
            {
              "id": "APP",
               "count":all,
                "api": "全量:",
              "success": "true",
              "x": 10,
              "y": 270
            },

            {
                "shape": "PHP",
              "id": "PHP",
              "success": "true",
              "count":2222,
              "x": 100,
              "y": 150
            },
            {
              "id": "list",
              "status": "php-list/GCI",
              "count":2222,
              "success": "true",
              "x": 350,
              "y": 150
            },

            {
                "shape": "zuul",
              "id": "zuul",
              "success": "true",
                "count":"2222",
              "x": 100,
              "y": 400
            },
            {
                "shape": "V2",
              "id": "all-api",
              "success": "true",
              "status": "all-api",
                "api": all_api_api,
                "count":all_api,
              "x": 350,
              "y": 300
            },
            {
                "shape": "V2",
              "id": "replay-api",
              "success": "true",
                "api":reply_api_api,
                "count":reply_api,
              "status": "replay-api",
              "x": 350,
              "y": 400
            },
            {
                "shape": "V2",
              "id": "thread-api",
              "success": "true",
              "count":thread_api,
                "api":thread_api_api,
              "status": "thread-api",
              "x": 350,
              "y": 500
            },

            {
              "id": "all-msv",
              "status": "all-msv",
                "count":"xxxxxx\nyyyyy\ndadasdasd\nasdadad",
              "success": "true",
              "x": 600,
              "y": 300
            },
            {
              "id": "replay-msv",
              "success": "true",
                "count":2222,
              "status": "eplay-msv",
              "x": 600,
              "y": 400
            },
            {
              "id": "thread-msv",
              "success": "true",
                "count":"",
              "status": "thread-msv",
              "x": 600,
              "y": 500
            },

            {
              "id": "zuul-db",
              "success": "true",
                "count":2222,
              "status": "zuul-db",
              "x": 850,
              "y": 400
            },

            {
              "id": "error",
              "success": "false",
              "x": 600,
              "y": 150
            }

          ],
          "edges": [
            {
              "shape": "customLine",
              "source": "APP",
              "id": "1",
                "precent": all_zuul,
              "target": "zuul"
            },

            {
              "shape": "customLine",
              "source": "zuul",
              "id": "2",
                "precent":all_api_sum,
              "target": "all-api"
            },
            {
              "shape": "customLine",
              "source": "zuul",
              "id": "3",
                "precent": thread_api_sum,
              "target": "thread-api"
            },
            {
              "shape": "customLine",
              "source": "zuul",
              "id": "4",
                "precent": reply_api_sum,
              "target": "replay-api"
            },

            {
              "shape": "customLine",
              "source": "replay-api",
              "id": "5",
              "target": "replay-msv"
            },
            {
              "shape": "customNodeV2",
              "source": "all-api",
              "id": "6",
              "target": "all-msv"
            },
            {
              "shape": "customLine",
              "source": "thread-api",
              "id": "7",
              "target": "thread-msv"
            },

            {
              "shape": "customEdge",
              "source": "thread-msv",
              "id": "8",
              "target": "zuul-db"
            },
            {
              "shape": "customEdge",
              "source": "all-msv",
              "id": "9",
              "target": "zuul-db"
            },
            {
              "shape": "customEdge",
              "source": "replay-msv",
              "id": "10",
              "target": "zuul-db"
            },

            {
              "shape": "customLine",
              "source": "APP",
              "id": "0f25fa89",
              "target": "PHP"
            },
            {
              "shape": "customLine",
              "source": "PHP",
              "id": "0f25fa90s",
              "target": "list"
            },
            {
              "shape": "customLine",
              "source": "list",
                "precent": 80,
              "id": "7cbab3c3",
              "target": "error"
            }
          ]
        }

    return  json.dumps(data)
