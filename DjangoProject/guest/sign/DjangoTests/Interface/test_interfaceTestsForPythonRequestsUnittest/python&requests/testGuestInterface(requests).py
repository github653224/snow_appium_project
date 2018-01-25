# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests,json

class GuestInterface:
    def testGetGuesttInterface(self,url,paramdict):
        self.url=url
        self.param=paramdict
        print "test start..."
        response=requests.get(self.url,params=self.param)
        result=response.json()
        print result
        assert result['status'] == 200
        assert result['message'] == "success"

        assert (result['data']['realname']) == "panxueyan"
        assert result['data']['phone'] == "18010193189"
        assert result['data']['email'] == "panxueyan@email.com"
        assert result['data']['sign'] == True
        print "test done"


if __name__=="__main__":
    url="http://127.0.0.1:8989/api/get_guest_list/"
    paramdict={
        "eid":"1",
        "phone":"18010193189"
    }
    event=GuestInterface()
    event.testGetGuesttInterface(url,paramdict)