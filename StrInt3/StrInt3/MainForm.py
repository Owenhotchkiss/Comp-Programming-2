import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.RoyalBlue
		self._button3.Location = System.Drawing.Point(360, 230)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(113, 89)
		self._button3.TabIndex = 15
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.RoyalBlue
		self._button2.Location = System.Drawing.Point(209, 233)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(107, 86)
		self._button2.TabIndex = 14
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.RoyalBlue
		self._button1.Location = System.Drawing.Point(49, 230)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(113, 89)
		self._button1.TabIndex = 13
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.CornflowerBlue
		self._textBox1.Location = System.Drawing.Point(141, 19)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 11
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DodgerBlue
		self._label3.Location = System.Drawing.Point(141, 52)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 10
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Blue
		self._label2.ForeColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(35, 52)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 9
		self._label2.Text = "Unique Letter:"
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Blue
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(35, 16)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 8
		self._label1.Text = "Enter Text:"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.SkyBlue
		self.ClientSize = System.Drawing.Size(509, 334)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "StrInt3"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		word = self._textBox1.Text.lower()
		for x in word:
		
		