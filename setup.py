#!/usr/bin/env python
#
# Distutils setup script for NLTK-Contrib
#
# Copyright (C) 2001-2011 NLTK Project
# Author: Steven Bird <sb@csse.unimelb.edu.au>
#         Edward Loper <edloper@gradient.cis.upenn.edu>
#         Ewan Klein <ewan@inf.ed.ac.uk>
# URL: <http://www.nltk.org/>
# For license information, see LICENSE.TXT

from distutils.core import setup

setup(
    #############################################
    ## Distribution Metadata
    name = "nltk_contrib",
    description = "NLTK-Contrib",
    
    version = '3.1',
    # platforms = <platforms>,
    
    #############################################
    ## Package List
    packages = ['nltk_contrib',
                'nltk_contrib.align',
                'nltk_contrib.bioreader',
                'nltk_contrib.classifier',
                'nltk_contrib.classifier.exceptions',
                'nltk_contrib.classifier_tests',
                'nltk_contrib.coref',
                'nltk_contrib.dependency',
                'nltk_contrib.fst',
                'nltk_contrib.fuf',
                'nltk_contrib.hadoop',
                'nltk_contrib.hadoop.hadooplib',
                'nltk_contrib.lambek',
                'nltk_contrib.lpath',
                'nltk_contrib.lpath.lpath',
                'nltk_contrib.lpath.at_lite',
                'nltk_contrib.misc',
                'nltk_contrib.mit',
                'nltk_contrib.mit.six863',
                'nltk_contrib.mit.six863.kimmo',
                'nltk_contrib.mit.six863.parse',
                'nltk_contrib.mit.six863.semantics',
                'nltk_contrib.mit.six863.tagging',
                'nltk_contrib.readability',
                'nltk_contrib.refexpr',
                'nltk_contrib.rte',
                'nltk_contrib.scripttranscriber',
                'nltk_contrib.tag',
                'nltk_contrib.tiger',
                'nltk_contrib.tiger.indexer',
                'nltk_contrib.tiger.query',
                'nltk_contrib.tiger.utils',
                'nltk_contrib.toolbox'
                ],
    install_requires = ['setuptools', 'nltk']
    )
