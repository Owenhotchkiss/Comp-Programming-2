import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label6 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._comboBox3 = System.Windows.Forms.ComboBox()
		self._comboBox2 = System.Windows.Forms.ComboBox()
		self._label3 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._label1 = System.Windows.Forms.Label()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._radioButton4 = System.Windows.Forms.RadioButton()
		self._radioButton5 = System.Windows.Forms.RadioButton()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(415, 27)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 23
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.LightPink
		self._label6.Location = System.Drawing.Point(294, 27)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 22
		self._label6.Text = "Number of Shades:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.DeepPink
		self._label5.Location = System.Drawing.Point(161, 187)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 21
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Crimson
		self._label4.Location = System.Drawing.Point(44, 187)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 20
		self._label4.Text = "Your total is:"
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Orchid
		self._button2.Location = System.Drawing.Point(161, 239)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(126, 65)
		self._button2.TabIndex = 19
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Orchid
		self._button1.Location = System.Drawing.Point(29, 239)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(126, 64)
		self._button1.TabIndex = 18
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# comboBox3
		# 
		self._comboBox3.FormattingEnabled = True
		self._comboBox3.Items.AddRange(System.Array[System.Object](
			["7.75 axle",
			"8 axle",
			"8.5 axle"]))
		self._comboBox3.Location = System.Drawing.Point(150, 68)
		self._comboBox3.Name = "comboBox3"
		self._comboBox3.Size = System.Drawing.Size(121, 21)
		self._comboBox3.TabIndex = 17
		# 
		# comboBox2
		# 
		self._comboBox2.FormattingEnabled = True
		self._comboBox2.Items.AddRange(System.Array[System.Object](
			["51 mm",
			"55 mm",
			"58 mm",
			"61 mm"]))
		self._comboBox2.Location = System.Drawing.Point(150, 127)
		self._comboBox2.Name = "comboBox2"
		self._comboBox2.Size = System.Drawing.Size(121, 21)
		self._comboBox2.TabIndex = 16
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.LightPink
		self._label3.Location = System.Drawing.Point(44, 71)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 15
		self._label3.Text = "Truck Assemblies:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.LightPink
		self._label2.Location = System.Drawing.Point(44, 127)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 14
		self._label2.Text = "Wheel Sets:"
		# 
		# comboBox1
		# 
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Items.AddRange(System.Array[System.Object](
			["Master Thrasher",
			"The Dictator of Grind",
			"The Street King"]))
		self._comboBox1.Location = System.Drawing.Point(150, 24)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(121, 21)
		self._comboBox1.TabIndex = 13
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Pink
		self._label1.Location = System.Drawing.Point(44, 24)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 12
		self._label1.Text = "Deck:"
		# 
		# radioButton2
		# 
		self._radioButton2.BackColor = System.Drawing.Color.Khaki
		self._radioButton2.Location = System.Drawing.Point(306, 111)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(104, 24)
		self._radioButton2.TabIndex = 25
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Bearings"
		self._radioButton2.UseVisualStyleBackColor = False
		# 
		# radioButton3
		# 
		self._radioButton3.BackColor = System.Drawing.Color.Khaki
		self._radioButton3.Location = System.Drawing.Point(306, 164)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(104, 24)
		self._radioButton3.TabIndex = 26
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Riser Pads"
		self._radioButton3.UseVisualStyleBackColor = False
		# 
		# radioButton4
		# 
		self._radioButton4.BackColor = System.Drawing.Color.Khaki
		self._radioButton4.Location = System.Drawing.Point(306, 212)
		self._radioButton4.Name = "radioButton4"
		self._radioButton4.Size = System.Drawing.Size(104, 24)
		self._radioButton4.TabIndex = 27
		self._radioButton4.TabStop = True
		self._radioButton4.Text = "Nuts & Bolts Kits"
		self._radioButton4.UseVisualStyleBackColor = False
		# 
		# radioButton5
		# 
		self._radioButton5.BackColor = System.Drawing.Color.Khaki
		self._radioButton5.Location = System.Drawing.Point(306, 259)
		self._radioButton5.Name = "radioButton5"
		self._radioButton5.Size = System.Drawing.Size(104, 24)
		self._radioButton5.TabIndex = 28
		self._radioButton5.TabStop = True
		self._radioButton5.Text = "Assembly"
		self._radioButton5.UseVisualStyleBackColor = False
		# 
		# radioButton1
		# 
		self._radioButton1.BackColor = System.Drawing.Color.Khaki
		self._radioButton1.Location = System.Drawing.Point(306, 71)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(104, 24)
		self._radioButton1.TabIndex = 29
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Grip Tape"
		self._radioButton1.UseVisualStyleBackColor = False
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(848, 329)
		self.Controls.Add(self._radioButton1)
		self.Controls.Add(self._radioButton5)
		self.Controls.Add(self._radioButton4)
		self.Controls.Add(self._radioButton3)
		self.Controls.Add(self._radioButton2)
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
		self.Text = "pg485skateboarddesigner"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		price = 0
		deckPrice = 0
		truckPrice = 0
		wheelPrice = 0
		miscPrice = 0
		
		numShades = int(self._textBox1.Text)
		if self._comboBox1.Text == "Regular Shades":
			stylePrice = 0
		elif self._comboBox1.Text == "Folding Shades":
			stylePrice = 10
		elif self._comboBox1.Text == "Roman Shades":
			stylePrice = 15
		if self._comboBox2.Text == "25 in":
			sizePrice = 0
		elif self._comboBox2.Text == "27 in":
			sizePrice = 2
		elif self._comboBox2.Text == "32 in":
			sizePrice = 4
		elif self._comboBox2.Text == "40 in":
			sizePrice = 6
		if self._comboBox3.Text == "Natural":
			colorPrice = 5
		else:
			colorPrice = 0
		if self._radioButton1.Checked:
			miscPrice = miscPrice + 10
		elif radiobutton2.Checked:
			miscPrice = miscPrice + 30
		elif radiobutton2.Checked:
			miscPrice = miscPrice + 2
		elif radiobutton2.Checked:
			miscPrice = miscPrice + 3
		elif radiobutton2.Checked:
			miscPrice = miscPrice + 10
		
		price = (numShades * 50) + stylePrice + sizePrice + colorPrice + miscPrice
		self._label5.Text = str(price)
		