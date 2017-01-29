Parcellite - Lightweight GTK+ Clipboard Manager
---
<a href="https://scan.coverity.com/projects/zawertun-parcellite">
  <img alt="Coverity Scan Build Status"
       src="https://scan.coverity.com/projects/11608/badge.svg"/>
</a>

Copyright (C) 2007-2008 Gilberto "Xyhthyx" Miralla <xyhthyx@gmail.com>

Copyright (C) 2009-2016 Doug Springer <gpib@rickyrockrat.net>

Introduction
---
Parcellite is a lightweight GTK+ clipboard manager. This is a stripped down,
basic-features-only clipboard manager with a small memory footprint for those
who like simplicity. 

Project website: https://github.com/ZaWertun/parcellite

Compile and install
---

Build requirements:
* `cmake`
* `libX11`
* `gtk+ >= 2.10.0`

Runtime requirements:
* `xdotool` - to autopaste selected value.

Build instructions:
```bash
git clone https://github.com/ZaWertun/parcellite.git
cd parcellite
mkdir build && cd build && cmake -DCMAKE_INSTALL_PREFIX=/usr ..
make -j`nproc --all`
```

To install run:
```bash
sudo make install
```
