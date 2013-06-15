# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from scrapy.contrib.exporter import XmlItemExporter

class conEtiquetaPipeline(object):
    """ Las entradas que tienen etiqueta las pasa al archivo entradas_etiquetadas.xml """

    def __init__(self):
        dispatcher.connect(self.spider_opened, signals.spider_opened)
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def spider_opened(self, spider):

        # fichero de guardado
        self.file = open('entradas_etiquetadas.xml', 'w+b')

        self.exporter = XmlItemExporter(self.file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
    
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
		""" si el item tiene una etiqueta lo exporta al archivo prefijado """
		if item['etiquetas']:
			self.exporter.export_item(item)
		return item

class sinEtiquetaPipeline(object):
	""" Las entradas que tienen etiqueta las pasa al archivo entradas_no_etiquetadas.xml """
	def __init__(self):
		dispatcher.connect(self.spider_opened, signals.spider_opened)
		dispatcher.connect(self.spider_closed, signals.spider_closed)

	def spider_opened(self, spider):
		
		# fichero de guardado
		self.file = open('entradas_no_etiquetadas.xml', 'w+b')
		
		self.exporter = XmlItemExporter(self.file)
		self.exporter.start_exporting()

	def spider_closed(self, spider):
		self.exporter.finish_exporting()
		self.file.close()

	def process_item(self, item, spider):
		""" si el item tiene una etiqueta lo exporta al archivo prefijado """
		if not item['etiquetas']:
			self.exporter.export_item(item)
		return item
  


