import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._label3 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.SystemColors.Info
		self._textBox1.Location = System.Drawing.Point(118, 54)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.SystemColors.Info
		self._textBox2.Location = System.Drawing.Point(270, 51)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 1
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Orange
		self._label1.Location = System.Drawing.Point(12, 51)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 2
		self._label1.Text = "Enter a Number:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Orange
		self._label2.Location = System.Drawing.Point(376, 48)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 3
		self._label2.Text = "Enter a Number:"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button1.Location = System.Drawing.Point(95, 121)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(101, 85)
		self._button1.TabIndex = 4
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button2.Location = System.Drawing.Point(302, 121)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(101, 85)
		self._button2.TabIndex = 5
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Gold
		self._label3.Location = System.Drawing.Point(129, 235)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(225, 47)
		self._label3.TabIndex = 6
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(488, 313)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "pg266largesmall"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		if num1 > num2:
			self._label3.Text = str(num1)
		elif num1 < num2:
			self._label3.Text = str(num2)

	def Button2Click(self, sender, e):
		Application.Exit()