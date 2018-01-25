# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests,json
class EventInterface:
    def testGetEventInterface(self,url,paramdict):
        self.url=url
        self.param=paramdict
        print "test start..."
        response=requests.get(self.url,params=self.param)
        result=response.json()
        # print result
        assert result['status'] == 200
        assert result['message'] == "success"

        if isinstance((result['data']),list):
            print "(result['data']) is list !"
            assert (result['data'][0]['name']) == "iPhone X发布会"
            assert result['data'][0]['address'] == "北京水立方"
            assert result['data'][0]['start_time'] == "2018-01-20T16:56:40"

            print "(result['data']) is list !"
            assert (result['data'][1]['name']) == "iPhone X发布会"
            assert result['data'][1]['address'] == "日本"
            assert result['data'][1]['start_time'] == "2018-01-25T13:25:34"
            print "test done"
        else:
            print "(result['data']) is not list !"
            assert (result['data']['name']) == "iPhone X发布会"
            assert result['data']['address'] == "北京水立方"
            assert result['data']['start_time'] == "2018-01-20T16:56:40"
            print "test done"


if __name__=="__main__":
    url="http://127.0.0.1:8989/api/get_event_list/"
    paramdict={
        # "eid":"1"
        "name":"iPhone X发布会"
    }
    event=EventInterface()
    event.testGetEventInterface(url,paramdict)