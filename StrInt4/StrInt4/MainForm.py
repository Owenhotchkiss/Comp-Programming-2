import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Moccasin
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(122, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Type a word"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkOrchid
		self._button1.Location = System.Drawing.Point(12, 52)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(122, 45)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label2.Location = System.Drawing.Point(12, 125)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(122, 23)
		self._label2.TabIndex = 2
		self._label2.Text = "The word reversed:"
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DarkOrchid
		self._button2.Location = System.Drawing.Point(140, 52)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(122, 45)
		self._button2.TabIndex = 3
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Orange
		self._label3.Location = System.Drawing.Point(140, 9)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(122, 23)
		self._label3.TabIndex = 4
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.CornflowerBlue
		self._label4.Location = System.Drawing.Point(140, 125)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(122, 23)
		self._label4.TabIndex = 5
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(291, 212)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "StrInt4"
		self.ResumeLayout(False)


	def Button2Click(self, sender, e):
		Application.Exit()