#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#pylint:disable=W0301
#
#  Copyright 2018- William Martinez Bas <metfar@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor,
#  MA 02110-1301, USA.
#
# ---------------------------------------------------------------------
# Package:			includes
# File:				core.py
# Version:			0.8.4
# Description;		allows to import using include/includes
# ---------------------------------------------------------------------

import os;
import warnings;
warnings.filterwarnings(
	"ignore",
	message="Your system is avx2 capable",
	category=RuntimeWarning
);
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1";
null=Null=NULL=Nil=None;
on=On=ON=true=TRUE=True;
off=Off=OFF=false=FALSE=False;
INFO=Info=2;
DBG=off;

def debug(value=null):
    global DBG;
    if (value is null):
        try:
            if (DBG is null):
                DBG=off;
        except:
            DBG=off;
        return(DBG);
    try:
        DBG=value;
    except:
        DBG=off;
    return(DBG);

def include(f):
	content=f.split();
	
	if("from" in f.lower()):
		if(content[1]=="from"):
			x="from "+content[2]+" import "+content[0]+" "+" ".join(content[3:]);
			lib=content[2];
	else:
		x="import "+f;
		lib=content[0] if len(content)>2 else f;

	if ("pygame" in f.lower()):
		warnings.filterwarnings(
			"ignore",
			category=UserWarning,
			module="pygame.pkgdata"
		);
	try:
		if(debug()>=2):
			print(x);
		exec(x);
		if(debug()>=1):
			print(f"{lib} included");
		return(True);
	except:
		if(debug()>=1):
			print(f"{lib} included");
		return(False);

def includes(*argv):
	args=[];
	for f in argv:
		if (type(f)==type([])):
			for n in f:
				args.append(n);
		else:
			args.append(f);
	if(type(args)==type("")):
		include(args);
	else:
		for f in args:
			include(f);

if __name__ == "__main__":
	debug(on);
	for f in ["numpy as np","pygame","pygame as pg","* from sys"]:
	   include(f);
	includes(["numpy as np","time","pygame as pg","* from sys"]);
