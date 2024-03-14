import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._comboBox2 = System.Windows.Forms.ComboBox()
		self._comboBox3 = System.Windows.Forms.ComboBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkTurquoise
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Styles:"
		# 
		# comboBox1
		# 
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Items.AddRange(System.Array[System.Object](
			["Regular Shades",
			"Folding Shades",
			"Roman Shades"]))
		self._comboBox1.Location = System.Drawing.Point(118, 9)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(121, 21)
		self._comboBox1.TabIndex = 1
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DarkTurquoise
		self._label2.Location = System.Drawing.Point(12, 112)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 2
		self._label2.Text = "Colors:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DarkTurquoise
		self._label3.Location = System.Drawing.Point(12, 56)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 3
		self._label3.Text = "Sizes:"
		# 
		# comboBox2
		# 
		self._comboBox2.FormattingEnabled = True
		self._comboBox2.Items.AddRange(System.Array[System.Object](
			["Natural",
			"Blue",
			"Teal",
			"Red",
			"Green"]))
		self._comboBox2.Location = System.Drawing.Point(118, 112)
		self._comboBox2.Name = "comboBox2"
		self._comboBox2.Size = System.Drawing.Size(121, 21)
		self._comboBox2.TabIndex = 4
		# 
		# comboBox3
		# 
		self._comboBox3.FormattingEnabled = True
		self._comboBox3.Items.AddRange(System.Array[System.Object](
			["25 in",
			"27 in",
			"32 in",
			"40 in"]))
		self._comboBox3.Location = System.Drawing.Point(118, 53)
		self._comboBox3.Name = "comboBox3"
		self._comboBox3.Size = System.Drawing.Size(121, 21)
		self._comboBox3.TabIndex = 5
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.PaleTurquoise
		self._button1.Location = System.Drawing.Point(103, 224)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(126, 64)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.PaleTurquoise
		self._button2.Location = System.Drawing.Point(312, 224)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(126, 65)
		self._button2.TabIndex = 7
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = False
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DeepSkyBlue
		self._label4.Location = System.Drawing.Point(12, 172)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 8
		self._label4.Text = "Your total is:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.CornflowerBlue
		self._label5.Location = System.Drawing.Point(129, 172)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 9
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.DarkTurquoise
		self._label6.Location = System.Drawing.Point(262, 12)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 10
		self._label6.Text = "Number of Shades:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(383, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 11
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Teal
		self.ClientSize = System.Drawing.Size(493, 300)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._comboBox3)
		self.Controls.Add(self._comboBox2)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._comboBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "pg485ShadeDesigner"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		price = 0
		stylePrice = 0
		sizePrice = 0
		colorPrice = 0
		numShades = int(self._textBox1.Text)
		if comboBox1.Text == "Regular Shades":
			stylePrice = 0
		elif comboBox1.Text == "Folding Shades":
			stylePrice = 10
		elif comboBox1.Text == "Roman Shades":
			stylePrice = 15
		if comboBox2.Text == "25 in":
			sizePrice = 0
		elif comboBox2.Text == "27 in":
			sizePrice = 2
		elif comboBox2.Text == "32 in":
			sizePrice = 4
		elif comboBox2.Text == "40 in":
			sizePrice = 6
		if comboBox3.Text == "Natural":
			colorPrice = 5
		else:
			colorPrice = 0
		price = (numShades * 50) + stylePrice + sizePrice + colorPrice
		self._label5.Text = price
					