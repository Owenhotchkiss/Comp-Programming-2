
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
	def __init__(self, parent, msg):
		self.InitializeComponent()
		self.myparent = parent
		self.msg = msg
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(111, 82)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(111, 70)
		self._label1.TabIndex = 0
		self._label1.Text = "label1"
		self._label1.Click += self.Label1Click
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(81, 155)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(187, 113)
		self._button1.TabIndex = 1
		self._button1.Text = "Show Home Form"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# Form1
		# 
		self.ClientSize = System.Drawing.Size(435, 305)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "Form1"
		self.Text = "Form1"
		self.FormClosing += self.Form1FormClosing
		self.Load += self.Form1Load
		self.ResumeLayout(False)


	def Label1Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		self.Close()
		self.myparent.Show()

	def Form1Load(self, sender, e):
		self._label1.Text = self.msg

	def Form1FormClosing(self, sender, e):
		self.myparent.Show()