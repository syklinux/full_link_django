
from utils import es

a = es.post("api:/status/* AND host:games.mobileapi.hupu.com")
b = es.post("api:/forums/getForums AND host:bbs.mobileapi.hupu.com")


print(a,b)