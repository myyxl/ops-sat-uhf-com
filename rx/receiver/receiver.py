#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: OPS-SAT UHF RX
# Author: Fischer Benjamin, Mladenov Tom, Marlon Starkloff
# Description: UHF RX application
# GNU Radio version: 3.10.5.1

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
import math
from gnuradio import blocks
import pmt
from gnuradio import digital
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import zeromq
import gpredict
import satellites.components.deframers



from gnuradio import qtgui

class receiver(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "OPS-SAT UHF RX", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("OPS-SAT UHF RX")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "receiver")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.signal_freq = signal_freq = 437.2e6
        self.true_freq = true_freq = signal_freq
        self.samp_rate_down = samp_rate_down = 57.6e3
        self.samp_rate = samp_rate = 200e3
        self.offset_freq = offset_freq = -40e3
        self.doppler_freq = doppler_freq = true_freq - signal_freq
        self.baud_rate = baud_rate = 9600
        self.variable_low_pass_filter_taps_0 = variable_low_pass_filter_taps_0 = firdes.low_pass(1.0, samp_rate, 25000,1000, window.WIN_HAMMING, 6.76)
        self.squelch = squelch = -130
        self.gaussian_taps = gaussian_taps = firdes.gaussian (1.5, 2* (samp_rate_down / baud_rate) , 0.5, 12)
        self.gain_mu = gain_mu = 0.175
        self.freq_tuned = freq_tuned = offset_freq - doppler_freq

        ##################################################
        # Blocks
        ##################################################

        self.zeromq_pub_msg_sink_0 = zeromq.pub_msg_sink('tcp://127.0.0.1:5555', 100, True)
        self.satellites_ax25_deframer_0 = satellites.components.deframers.ax25_deframer(g3ruh_scrambler=True, options="")
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=int(samp_rate_down),
                decimation=int(samp_rate),
                taps=[],
                fractional_bw=0)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
            512, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "OPS-SAT UHF BEACON", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.03)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)



        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.qwidget(), Qt.QWidget)

        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.gpredict_doppler_1_0 = gpredict.doppler('localhost', 4532, True)
        self.gpredict_MsgPairToVar_0 = gpredict.MsgPairToVar(self.set_true_freq)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(1, variable_low_pass_filter_taps_0, (-freq_tuned), samp_rate)
        self.fir_filter_xxx_0 = filter.fir_filter_fff(1, gaussian_taps)
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(((samp_rate_down / baud_rate)*(1+0.0)), (0.25*gain_mu*gain_mu), 0.5, gain_mu, 0.005)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_message_debug_0 = blocks.message_debug(True)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/marlon/Desktop/gr-opssat/recordings/osat_437.16M_200k_beacon_mode6.cf32', True, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.analog_simple_squelch_cc_0 = analog.simple_squelch_cc(squelch, 1)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf((2 * (samp_rate_down / baud_rate) /(math.pi)))


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.gpredict_doppler_1_0, 'freq'), (self.blocks_message_debug_0, 'print'))
        self.msg_connect((self.gpredict_doppler_1_0, 'freq'), (self.gpredict_MsgPairToVar_0, 'inpair'))
        self.msg_connect((self.satellites_ax25_deframer_0, 'out'), (self.zeromq_pub_msg_sink_0, 'in'))
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.analog_simple_squelch_cc_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.analog_simple_squelch_cc_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.satellites_ax25_deframer_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_quadrature_demod_cf_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_waterfall_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "receiver")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_signal_freq(self):
        return self.signal_freq

    def set_signal_freq(self, signal_freq):
        self.signal_freq = signal_freq
        self.set_doppler_freq(self.true_freq - self.signal_freq)
        self.set_true_freq(self.signal_freq)

    def get_true_freq(self):
        return self.true_freq

    def set_true_freq(self, true_freq):
        self.true_freq = true_freq
        self.set_doppler_freq(self.true_freq - self.signal_freq)

    def get_samp_rate_down(self):
        return self.samp_rate_down

    def set_samp_rate_down(self, samp_rate_down):
        self.samp_rate_down = samp_rate_down
        self.set_gaussian_taps(firdes.gaussian (1.5, 2* (self.samp_rate_down / self.baud_rate) , 0.5, 12))
        self.analog_quadrature_demod_cf_0.set_gain((2 * (self.samp_rate_down / self.baud_rate) /(math.pi)))
        self.digital_clock_recovery_mm_xx_0.set_omega(((self.samp_rate_down / self.baud_rate)*(1+0.0)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_variable_low_pass_filter_taps_0(firdes.low_pass(1.0, self.samp_rate, 25000, 1000, window.WIN_HAMMING, 6.76))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_offset_freq(self):
        return self.offset_freq

    def set_offset_freq(self, offset_freq):
        self.offset_freq = offset_freq
        self.set_freq_tuned(self.offset_freq - self.doppler_freq)

    def get_doppler_freq(self):
        return self.doppler_freq

    def set_doppler_freq(self, doppler_freq):
        self.doppler_freq = doppler_freq
        self.set_freq_tuned(self.offset_freq - self.doppler_freq)

    def get_baud_rate(self):
        return self.baud_rate

    def set_baud_rate(self, baud_rate):
        self.baud_rate = baud_rate
        self.set_gaussian_taps(firdes.gaussian (1.5, 2* (self.samp_rate_down / self.baud_rate) , 0.5, 12))
        self.analog_quadrature_demod_cf_0.set_gain((2 * (self.samp_rate_down / self.baud_rate) /(math.pi)))
        self.digital_clock_recovery_mm_xx_0.set_omega(((self.samp_rate_down / self.baud_rate)*(1+0.0)))

    def get_variable_low_pass_filter_taps_0(self):
        return self.variable_low_pass_filter_taps_0

    def set_variable_low_pass_filter_taps_0(self, variable_low_pass_filter_taps_0):
        self.variable_low_pass_filter_taps_0 = variable_low_pass_filter_taps_0
        self.freq_xlating_fir_filter_xxx_0.set_taps(self.variable_low_pass_filter_taps_0)

    def get_squelch(self):
        return self.squelch

    def set_squelch(self, squelch):
        self.squelch = squelch
        self.analog_simple_squelch_cc_0.set_threshold(self.squelch)

    def get_gaussian_taps(self):
        return self.gaussian_taps

    def set_gaussian_taps(self, gaussian_taps):
        self.gaussian_taps = gaussian_taps
        self.fir_filter_xxx_0.set_taps(self.gaussian_taps)

    def get_gain_mu(self):
        return self.gain_mu

    def set_gain_mu(self, gain_mu):
        self.gain_mu = gain_mu
        self.digital_clock_recovery_mm_xx_0.set_gain_omega((0.25*self.gain_mu*self.gain_mu))
        self.digital_clock_recovery_mm_xx_0.set_gain_mu(self.gain_mu)

    def get_freq_tuned(self):
        return self.freq_tuned

    def set_freq_tuned(self, freq_tuned):
        self.freq_tuned = freq_tuned
        self.freq_xlating_fir_filter_xxx_0.set_center_freq((-self.freq_tuned))




def main(top_block_cls=receiver, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
