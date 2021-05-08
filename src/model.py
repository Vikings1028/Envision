'''
Application : Envision
File name   : model.py
Authors     : Jacob Summerville and Safwan Elmadani
Description : This file contains is used to include models
'''

# Copyright (c) April 26, 2021 Jacob Summerville and Safwan Elmadani
# All rights reserved.
#
# The license below extends only to copyright in the software and shall
# not be construed as granting a license to any other intellectual
# property including but not limited to intellectual property relating
# to a hardware implementation of the functionality of the software
# licensed hereunder.  You may use the software subject to the license
# terms below provided that you ensure that this notice is replicated
# unmodified and in its entirety in all distributions of the software,
# modified or unmodified, in source code or in binary form.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met: redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer;
# redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution;
# neither the name of the copyright holders nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from xml.dom import minidom 
import os, logging

from src.config.settings import config

class Model:
    """ This class is used to include models """

    def __init__(self):
        self.root  = config.root
        self.world = config.world

    def TextTag(self, parent, name, text):
        """ Creates a text tag and adds it to the parent """

        tag = self.root.createElement(name)
        tag_text = self.root.createTextNode(text) 
        tag.appendChild(tag_text)
        parent.appendChild(tag) 

    def AddModel(self, model, pose=None, name=None, static=None):
        """ Add a model to the world """

        logging.info('Adding Model -> ' + model)

        include = self.root.createElement('include')
        self.TextTag(include, 'uri', 'model://' + model) 

        if pose:
            self.TextTag(include, 'pose', pose) 

        if name:
            self.TextTag(include, 'name', name) 

        if static:
            self.TextTag(include, 'static', static) 

        self.world.appendChild(include)