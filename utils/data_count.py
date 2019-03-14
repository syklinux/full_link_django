# -*- coding: utf-8 -*-

import json


def conn(v):
    for key,value in v.items():
        if key == "all-api":
            all_api_all = []
            for i,j in value.items():
                a = (i + ":" + str(j) + '\n')
                all_api_all.append(a)
            all_api = (''.join(all_api_all))
        if key == "reply-api":
            reply_api_all = []
            for i, j in value.items():
                a = (i + ":" + str(j) + '\n')
                reply_api_all.append(a)
            reply_api = (''.join(reply_api_all))
        if key == "thread-api":
            thread_api_all = []
            for i, j in value.items():
                a = (i + ":" + str(j) + '\n')
                thread_api_all.append(a)
            thread_api = (''.join(thread_api_all))

    data = {
      "nodes": [
        {
          "shape": "initial",
          "id": "APP",
          "x": 10,
          "y": 270
        },
        {
          "shape": "normal",
          "id": "PHP",
          "status":"php",
          "x": 100,
          "y": 100
        },
        {
          "shape": "normal",
          "id": "list",
          "status": "php-list/GCI",
          "x": 300,
          "y": 100
        },

        {
          "shape": "normal",
          "id": "zuul",
          "status": "zuul",
          "x": 100,
          "y": 370
        },
        {
          "shape": "data",
          "id": "all-api",
          "status": all_api,
          "x": 400,
          "y": 270
        },
        {
          "shape": "data",
          "id": "reply-api",
          "status": reply_api,
          "x": 400,
          "y": 370
        },
        {
          "shape": "data",
          "id": "thread-api",
          "status": thread_api,
          "x": 400,
          "y": 470
        },

        {
          "shape": "normal",
          "id": "all-msv",
          "status": "all-msv",
          "x": 800,
          "y": 270
        },
        {
          "shape": "normal",
          "id": "reply-msv",
          "status": "reply-msv",
          "x": 800,
          "y": 370
        },
        {
          "shape": "normal",
          "id": "thread-msv",
          "status": "thread-msv",
          "x": 800,
          "y": 470
        },

        {
          "shape": "initial",
          "id": "zuul-db",
          "status": "zuul-db",
          "x": 1000,
          "y": 370
        },

        {
          "shape": "error",
          "id": "error",
          "status": "xxxxxx\nyyyyy\ndadasdasd\nasdadad",
          "x": 600,
          "y": 100
        }

      ],
      "edges": [
        {
          "shape": "customEdge",
          "source": "APP",
          "id": "1",
          "target": "zuul"
        },

        {
          "shape": "customEdge",
          "source": "zuul",
          "id": "2",
          "target": "all-api"
        },
        {
          "shape": "customEdge",
          "source": "zuul",
          "id": "3",
          "target": "thread-api"
        },
        {
          "shape": "customEdge",
          "source": "zuul",
          "id": "4",
          "target": "reply-api"
        },

        {
          "shape": "customEdge",
          "source": "reply-api",
          "id": "5",
          "target": "reply-msv"
        },
        {
          "shape": "customEdge",
          "source": "all-api",
          "id": "6",
          "target": "all-msv"
        },
        {
          "shape": "customEdge",
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
          "source": "reply-msv",
          "id": "10",
          "target": "zuul-db"
        },

        {
          "shape": "customEdge",
          "source": "APP",
          "id": "0f25fa89",
          "target": "PHP"
        },
        {
          "shape": "customEdge",
          "source": "PHP",
          "id": "0f25fa90s",
          "target": "list"
        },
        {
          "shape": "customEdge",
          "source": "list",
          "id": "7cbab3c3",
          "target": "error"
        }
      ]
    }


    return  json.dumps(data)

