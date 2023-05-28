import re
import chatbot2_extra as ex

def get_prio(bot_msg,res_set,single=False,require_set=[]):
    has_required=True
    count=0
    
    for word in bot_msg:
        if word in res_set:
            count+=1

    for word in require_set:
        if word not in bot_msg:
            has_required=False
    percent=float(count)/float(len(res_set))
    if single or has_required:
        return int(percent*100)
    else :
            return 0


def get_response_set(message):
    response_set={}

    def response(bot_res,res_Set,single=False,require_set=[]):
        nonlocal response_set
        response_set[bot_res]=get_prio(message,res_Set,single,require_set)
    response('Hello! ', ['hi','hello','hoi','whats up'],single=True)
    response('I am fine... ', ['how','are','you','fine'],require_set=['how'])
    response('Thanks', ['good','super','nice','wonderful'],single=True)
    response('I am a bot ...', ['who ','are','you',''],require_set=['who','are'])

    response(ex.eat,['eat','drink','you'],require_set=['you','eat'])
    response(ex.love,['love','do','you'],require_set=['you','love'])
    set_res=max(response_set,key=response_set.get)
    if response_set[set_res]<1:
        return ex.un()
    else:
        return set_res
    
    

def get_response(message):
    s=re.split(r'\s+|[,./<>?;:{}]\s*',message.lower())
    st=get_response_set(s)
    return st


while True:
    print('Bot :' + get_response(input('You : ')))

