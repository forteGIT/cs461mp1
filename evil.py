#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           �1��g:Ց���9�,�&��Q�B.z�F$��w+���	��.y�3V:*�;�5zH����1c���2�U�R�E�5.Ӗӵ�5�k���LU<�����m^wM���0~�DK��ӵ�kS���"""
from hashlib import sha256
if sha256(blob).hexdigest() == '07f57af135391fa9ff03c5defcbac75eaf8c848808c13af1e9dcaad87b182d7f':
	print 'I come in peace.'
else:
	print 'Prepare to be destroyed!'
