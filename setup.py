# Copyright (C) 2015-2018 Jurriaan Bremer <jbr@cuckoo.sh>
# Copyright (C) 2019 Hatching B.V.
# This file is part of HTTPReplay - http://jbremer.org/httpreplay/
# See the file 'LICENSE' for copying permission.

from setuptools import setup

setup(
    name="HTTPReplay",
    version="1.0.2",
    author="Hatching B.V.",
    author_email="info@hatching.io",
    packages=[
        "httpreplay",
    ],
    url="https://github.com/hatching/httpreplay",
    license="GPLv3",
    description="Properly interpret, decrypt, and replay pcap files",
    install_requires=[
        "dpkt>=1.9.6, <1.10",
        "tlslite-ng==0.8.1",
        "click>=8.1.2",
        "brotli==1.1.0, <1.2",
        "future"
    ],
    python_requires=">=3.10",
    extras_require={
        "mitmproxy": [
            "mitmproxy==4.0.4",
        ],
        "dev": [
            "mock==2.0.0",
            "pytest>=4.4.1"
        ]
    },
    entry_points={
        "console_scripts": [
            "httpreplay = httpreplay.main:httpreplay",
            "pcap2mitm = httpreplay.main:do_pcap2mitm",
        ]
    },
)
