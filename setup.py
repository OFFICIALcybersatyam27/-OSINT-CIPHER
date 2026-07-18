# -*- OFFICIAL_cyber_satyam27 -*-
"""
╔════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                            ║
║   ██████╗ ███████╗██╗███╗   ██╗████████╗     ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗    ║
║  ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝    ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗   ║
║  ██║   ██║███████╗██║██╔██╗ ██║   ██║       ██║     ██║██████╔╝███████║█████╗  ██████╔╝   ║
║  ██║   ██║╚════██║██║██║╚██╗██║   ██║       ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗   ║
║  ╚██████╔╝███████║██║██║ ╚████║   ██║       ╚██████╗██║██║     ██║  ██║███████╗██║  ██║   ║
║   ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝        ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ║
║                                                                                            ║
╠════════════════════════════════════════════════════════════════════════════════════════════╣
║                                ⚡ OSINT-CIPHER-SRY v1.61 ⚡                                ║
║                                                                                            ║
║  👑 Developer : 𒉭 ᎠᴀʀᴋㅤᏙᴇɴᴏᴍㅤ×͜× | 𝐓𝐇𝐄 𝐀𝐋𝐏𝐇𝐀 𒉭                                           ║
║  🛡 Brand     : OFFICIAL_cyber_satyam27                                                    ║
║  🌐 GitHub    : https://github.com/OFFICIALcybersatyam27                                   ║
║  ▶ YouTube   : https://youtube.com/@OFFICIAL_cyber_satyam27                                ║
║                                                                                            ║
║                    EDUCATIONAL • OSINT • RESEARCH • PYTHON TOOL                            ║
║                                                                                            ║
╚════════════════════════════════════════════════════════════════════════════════════════════╝
"""

from setuptools import setup, find_packages

setup(
    name='-OSINT-CIPHER',
    version="1.61",
    packages=find_packages(),
    author="𒉭 ᎠᴀʀᴋㅤᏙᴇɴᴏᴍㅤ×͜× | 𝐓𝐇𝐄 𝐀𝐋𝐏𝐇𝐀 𒉭",
    author_email="hackeriwy@gmail.com",
    install_requires=[
        "termcolor",
        "bs4",
        "httpx",
        "trio",
        "tqdm",
        "colorama"
    ],
    description="-OSINT-CIPHER allows you to check if the mail is used on different sites like Twitter, Instagram, Snapchat and other supported services.",
    include_package_data=True,
    url='https://github.com/OFFICIALcybersatyam27',
    entry_points = {'console_scripts': ['OSINT CIPHER SRY = holehe.core:main']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)