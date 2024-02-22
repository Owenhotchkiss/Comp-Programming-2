import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label8 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label6 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.PowderBlue
		self._label8.Location = System.Drawing.Point(115, 212)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 38
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.PowderBlue
		self._label7.Location = System.Drawing.Point(115, 159)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 37
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Turquoise
		self._button3.Location = System.Drawing.Point(268, 214)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(185, 45)
		self._button3.TabIndex = 36
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Turquoise
		self._button2.Location = System.Drawing.Point(363, 159)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(90, 49)
		self._button2.TabIndex = 35
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Turquoise
		self._button1.Location = System.Drawing.Point(268, 161)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(89, 47)
		self._button1.TabIndex = 34
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.PowderBlue
		self._textBox1.Location = System.Drawing.Point(115, 71)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 33
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.CornflowerBlue
		self._label6.Location = System.Drawing.Point(9, 212)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 32
		self._label6.Text = "Circumfrence:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.CornflowerBlue
		self._label5.Location = System.Drawing.Point(9, 159)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 31
		self._label5.Text = "Area:"
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.CornflowerBlue
		self._label1.Location = System.Drawing.Point(9, 71)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 30
		self._label1.Text = "Radius:"
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(457, 267)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "prog54cfunc"
		self.ResumeLayout(False)
		self.PerformLayout()

