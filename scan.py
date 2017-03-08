#!/usr/bin/python
from socket import gethostbyname, AF_INET
a=raw_input('Insert Target \t')
target=gethostbyname(a)
print target
