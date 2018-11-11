# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 17:37:25 2018

@author: 王磊
"""

import builtwith
import whois

pa = builtwith.parse('https://www.hacg.wiki/')

who = whois.query('https://www.hacg.wiki/')