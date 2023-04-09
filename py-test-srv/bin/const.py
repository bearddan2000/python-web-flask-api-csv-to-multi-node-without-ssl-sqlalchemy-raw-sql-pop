URL = 'http://py-srv-post:5000'

GET_ALL_URL = URL + '/pop'

GET_ALL = {
  "results": [
    {
      "color": "orange",
      "id": 1,
      "name": "Orange"
    },
    {
      "color": "purple",
      "id": 2,
      "name": "Grape"
    },
    {
      "color": "blue",
      "id": 3,
      "name": "Blueberry"
    },
    {
      "color": "red",
      "id": 4,
      "name": "Strawberry"
    }
  ]
}

UNSUPPORTED = {
  "results": "This action is unsupported"
}

DELETE_URL = URL + '/pop/1'

INSERT_URL = URL + '/pop/pink/lemonade'

SMOKE_URL = URL + '/'

SMOKE = {"hello": "world"}

UPDATE_URL = URL + '/pop/2/clear/crystal'
