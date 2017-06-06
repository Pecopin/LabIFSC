#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from LabIFSC import Medida

def test_medida_format_A1():
    m = Medida((31.5467, 1.52), "ft^2")
    assert "{}".format(m) == "32±2 ft²"
    m = Medida((31.5467, 0.052), "ft^2")
    assert "{}".format(m) == "31.55±0.05 ft²"

def test_medida_format_A2():
    m = Medida((31.5467, 1.52), "ft^2")
    assert "{:latex}".format(m) == "32\pm2\\textrm{ ft^2}"

def test_medida_format_A3():
    m = Medida((31.5467, 1.52), "ft^2")
    assert "{:latex-si}".format(m) == "\SI{32+-2}{\\foot\\squared}"

def test_medida_format_A4():
    m = Medida((31.5467, 1.52), "ft^2")
    assert "{}".format(m) == "32±2 ft²"

def test_medida_format_A5():
    m = Medida((31.5467, 1.52), "ft^2")
    assert "{:ascii}".format(m) == "32+/-2 ft^2"

def test_medida_format_B1():
    m = Medida((31.5467, 1.52), "ft^2")
    assert "{:-,full}".format(m) == "31.5467±1.52 ft²"

def test_medida_format_B2():
    m = Medida((31.5467, 1.52), "ft^2")
    assert "{:latex,full}".format(m) == "31.5467\pm1.52\\textrm{ ft^2}"

def test_medida_format_B3():
    m = Medida((31.5467, 1.52), "ft^2")
    assert "{:latex-si,full}".format(m) == "\SI{31.5467+-1.52}{\\foot\\squared}"

def test_medida_format_B4():
    m = Medida((31.5467, 1.52), "ft^2")
    assert "{:-,full}".format(m) == "31.5467±1.52 ft²"

def test_medida_format_B5():
    m = Medida((31.5467, 1.52), "ft^2")
    assert "{:ascii,full}".format(m) == "31.5467+/-1.52 ft^2"

def test_medida_format_C1():
    m = Medida((31.5467, 1.52), "ft^2")
    assert "{:repr}".format(m) == "<31.5467±1.52 ft² = {}±{} L2>".format(m.si_nominal, m.si_incerteza)