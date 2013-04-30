#!/usr/bin/python

from PySide.QtGui import QListWidget, QListWidgetItem, QVBoxLayout, QPushButton, QIcon, QMainWindow, QApplication, QFileDialog
from PySide.QtCore import Slot, QSize
from mainwindow import Ui_MainWindow

import sys, csv, time, os, warnings

from matplotlib import rc, pyplot as plt
rc('axes',edgecolor='0.5')
import numpy

# some default configuration parameters
_factor = 2.
_size = 75
_gain = 1.

class MainWindow(QMainWindow):
	app = None
	ui = None
	temp_pngs = []
	gain = 1.
	filename = None
	
	def __init__(self, application, parent=None):
		super(MainWindow, self).__init__(parent)
		self.app = application
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		
		self.ui.openButton.clicked.connect(self.open_file)
		self.ui.incGainBtn.clicked.connect(self.increase_gain)
		self.ui.decGainBtn.clicked.connect(self.decrease_gain)
		self.ui.copyButton.clicked.connect(self.copy_selections)
		
	@Slot()
	def copy_selections(self):
		items = self.ui.listWidget.selectedItems()
		channel_numbers = ' '.join([item.text() for item in items])
		cb = self.app.clipboard()
		cb.setText(channel_numbers)
		print 'Selection "%s" copied.' % channel_numbers
		
	@Slot()
	def open_file(self, filename=None):
		if not filename:
			filename, t = QFileDialog.getOpenFileName(filter='dat file (*.dat);; any file (*.*)', caption='Select a dat file')

		if filename != '':
			print 'Opening %s...' % filename
			self.gain = _gain
			self.draw_dat(filename)
			self.set_filename(filename)

	def set_filename(self, filename):
		if filename:
			self.filename = filename
			self.setWindowTitle('dat File Viewer [%s]' % self.filename)

	def draw_dat(self, filename=None, size=_size, gain=None):
		if filename == None:
			filename = self.filename
		if gain == None:
			gain = self.gain

		if filename != None:
			with open(filename, 'r') as fp:
				self.empty_list()
				self.plot_traces(fp, size, gain)

	def plot_traces(self, fp, size, gain):
		t0 = time.time()
		
		reader = csv.reader(fp, delimiter='\t')
		rows = [row for row in reader]
		n_channels = len(rows[0])
		count = len(rows)
		# possible trailing space in dat
		if rows[0][-1].strip() == '':
			n_channels -= 1

		traces = [numpy.array([float(row[i]) for row in rows]) for i in xrange(n_channels)]
		minimum = min(map(lambda x: x.min(), traces))
		maximum = max(map(lambda x: x.max(), traces))
		lw = self.ui.listWidget
		lw.setIconSize(QSize(size, size))
		for i, trace in enumerate(traces):
			icon = QIcon(self.gen_fig_png(trace, maximum / gain, minimum / gain, count))
			item = QListWidgetItem(icon, str(i+1))
			lw.addItem(item)
			
		print 'Done rendering traces in %.2fs.' % (time.time() - t0)
		
	def gen_fig_png(self, trace, maximum, minimum, count):
		with warnings.catch_warnings():
			warnings.simplefilter('ignore')
			png_path = '%s.png' % os.tempnam()
		plt.plot(trace, color='black', linewidth=4.)
		
		# artistic adjustment
		fig = plt.gcf()
		fig.set_size_inches(1, 1)
		ax = plt.gca()
		ax.set_ylim([minimum, maximum])
		ax.get_xaxis().set_visible(False)
		ax.get_yaxis().set_visible(False)
		
		# save figure to a temp file
		plt.savefig(png_path, bbox_inches=0., dpi=count)
		plt.close()
		
		self.temp_pngs.append(png_path)
		return png_path
	
	@Slot()
	def increase_gain(self, factor=_factor):
		self.gain *= factor
		print 'Gain = %.2f' % self.gain
		self.draw_dat(gain=self.gain)
	
	@Slot()
	def decrease_gain(self, factor=_factor):
		self.gain /= factor
		print 'Gain = %.2f' % self.gain
		self.draw_dat(gain=self.gain)
	
	def dragEnterEvent(self, event):
		if event.mimeData().hasFormat('text/uri-list'):
			event.acceptProposedAction()
		
	def dropEvent(self, event):
		# takes in one file by drag and drop
		self.open_file(event.mimeData().urls()[0].path())
		event.acceptProposedAction()
		
	def empty_list(self):
		self.ui.listWidget.clear()
		self.cleanup()
		
	def cleanup(self):
		# remove all created temp files
		if len(self.temp_pngs) > 0:
			print 'Removing all temp files...'
			fn = self.temp_pngs.pop()
			while len(self.temp_pngs) > 0:
				os.remove(self.temp_pngs.pop())
			print 'Done Removing.'
		
  	
if __name__ == "__main__":
  app = QApplication(sys.argv)
  mw = MainWindow(app)
  mw.show()
  app.exec_()
  mw.cleanup()
  sys.exit()
