#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .geral import TODAS_AS_UNIDADES, parse_dimensions, acha_unidade, dimensao_em_texto, gera_expoente

class Unidade:
    nome = ""
    simbolo = ""
    simbolo_latex = ""
    # As dimensões são (comprimento, ângulo, massa, tempo, temperatura, corrente, mol)
    dimensao = (0, 0, 0, 0, 0, 0, 0)
    # Valor que deve ser multiplicado para obter o valor no MKS
    cte_multiplicativa = None
    # Valor que deve ser adicionado para obter o valor no MKS
    cte_aditiva = None
    unidade_pai = None
    expoente_pai = None

    def __init__(self, nome, simbolo, simbolo_latex, dimensao, cte_multiplicativa, cte_aditiva):
        self.nome = str(nome).replace(" ", "_")
        self.simbolo = str(simbolo)
        self.simbolo_latex = str(simbolo_latex)

        self.cte_multiplicativa = cte_multiplicativa
        self.cte_aditiva = cte_aditiva
        if isinstance(dimensao, tuple):
            self.dimensao = dimensao
        else:
            self.dimensao = parse_dimensions(dimensao)

        self.unidade_pai = self
        self.expoente_pai = 1

        # Registre unidade
        global TODAS_AS_UNIDADES
        TODAS_AS_UNIDADES[nome.lower()] = self
        if simbolo.lower() not in TODAS_AS_UNIDADES:
            TODAS_AS_UNIDADES[simbolo] = self

    def __hash__(self):
        return hash(self.nome)

    def __str__(self):
        return self.nome

    def __eq__(self, other):
        if isinstance(other, Unidade):
            return self.nome == other.nome
        return False
    def nova_unidade_por_expoente(self, e):
        global TODAS_AS_UNIDADES

        # Veja os casos triviais
        if e == 1:
            return self
        if e == 0:
            return None
        if self.simbolo+gera_expoente(e) in TODAS_AS_UNIDADES:
            return TODAS_AS_UNIDADES[self.simbolo+gera_expoente(e)]
        if self.nome+"^"+str(e) in TODAS_AS_UNIDADES:
            return TODAS_AS_UNIDADES[self.nome+"^"+str(e)]

        # Gere a nova unidade
        cte_m = self.cte_multiplicativa**e
        cte_a = self.cte_aditiva
        dim = tuple([x*e for x in self.dimensao])
        u = Unidade(self.nome+"^"+str(e), self.simbolo+gera_expoente(e), self.simbolo_latex+"^"+str(e), dim, cte_m, cte_a)
        u.unidade_pai = self
        u.expoente_pai = e
        return u

    def __repr__(self):
        try:
            return "<{}:*{}:+{}:{}>".format(self.nome, self.cte_multiplicativa.nominal, self.cte_aditiva.nominal, dimensao_em_texto(self.dimensao))
        except:
            return "<{}:*?:+?:{}>".format(self.nome, dimensao_em_texto(self.dimensao))