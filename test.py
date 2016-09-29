#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication
from QxtSpanSlider import QxtSpanSlider


app = QApplication(sys.argv)
slider = QxtSpanSlider(None)
slider.setRange(0, 100)
slider.setSpan(30, 70)
slider.show()
sys.exit(app.exec_())
