import logging

class CallbackHandler(logging.StreamHandler):
	callback = None

	def emit(self, record):
		try:
			msg = self.format(record)
			if self.callback:
				self.callback(msg)
			self.flush()
		except (KeyboardInterrupt, SystemExit):
			raise
		except:
			self.handleError(record)