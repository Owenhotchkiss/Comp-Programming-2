import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
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
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._checkBox3 = System.Windows.Forms.CheckBox()
		self._checkBox4 = System.Windows.Forms.CheckBox()
		self._checkBox5 = System.Windows.Forms.CheckBox()
		self.SuspendLayout()
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
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Crimson
		self._label6.Location = System.Drawing.Point(310, 24)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 30
		self._label6.Text = "Sales tax is:"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.HotPink
		self._label7.Location = System.Drawing.Point(416, 24)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 31
		# 
		# checkBox1
		# 
		self._checkBox1.BackColor = System.Drawing.Color.Khaki
		self._checkBox1.Location = System.Drawing.Point(310, 65)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(104, 24)
		self._checkBox1.TabIndex = 32
		self._checkBox1.Text = "Grip Tape"
		self._checkBox1.UseVisualStyleBackColor = False
		# 
		# checkBox2
		# 
		self._checkBox2.BackColor = System.Drawing.Color.Khaki
		self._checkBox2.Location = System.Drawing.Point(310, 110)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(104, 24)
		self._checkBox2.TabIndex = 33
		self._checkBox2.Text = "Bearings"
		self._checkBox2.UseVisualStyleBackColor = False
		# 
		# checkBox3
		# 
		self._checkBox3.BackColor = System.Drawing.Color.Khaki
		self._checkBox3.Location = System.Drawing.Point(310, 161)
		self._checkBox3.Name = "checkBox3"
		self._checkBox3.Size = System.Drawing.Size(104, 24)
		self._checkBox3.TabIndex = 34
		self._checkBox3.Text = "Riser Pads"
		self._checkBox3.UseVisualStyleBackColor = False
		# 
		# checkBox4
		# 
		self._checkBox4.BackColor = System.Drawing.Color.Khaki
		self._checkBox4.Location = System.Drawing.Point(310, 208)
		self._checkBox4.Name = "checkBox4"
		self._checkBox4.Size = System.Drawing.Size(104, 24)
		self._checkBox4.TabIndex = 35
		self._checkBox4.Text = "Nuts & Bolts Kits"
		self._checkBox4.UseVisualStyleBackColor = False
		# 
		# checkBox5
		# 
		self._checkBox5.BackColor = System.Drawing.Color.Khaki
		self._checkBox5.Location = System.Drawing.Point(310, 260)
		self._checkBox5.Name = "checkBox5"
		self._checkBox5.Size = System.Drawing.Size(104, 24)
		self._checkBox5.TabIndex = 36
		self._checkBox5.Text = "Assembly"
		self._checkBox5.UseVisualStyleBackColor = False
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(536, 329)
		self.Controls.Add(self._checkBox5)
		self.Controls.Add(self._checkBox4)
		self.Controls.Add(self._checkBox3)
		self.Controls.Add(self._checkBox2)
		self.Controls.Add(self._checkBox1)
		self.Controls.Add(self._label7)
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


	def Button1Click(self, sender, e):
		price = 0
		tax = 0
		deckPrice = 0
		truckPrice = 0
		wheelPrice = 0
		miscPrice = 0
		
		if self._comboBox1.Text == "The Master Thrasher":
			deckPrice = 60
		elif self._comboBox1.Text == "The Dictator of Grind":
			deckPrice = 45
		elif self._comboBox1.Text == "The Street King":
			deckPrice = 50
		if self._comboBox2.Text == "7.75 axle":
			truckPrice = 35
		elif self._comboBox2.Text == "8 axle":
			truckPrice = 40
		elif self._comboBox2.Text == "8.5 axle":
			truckPrice = 45
		if self._comboBox3.Text == "51 mm":
			wheelPrice = 20
		elif self._comboBox3.Text == "55 mm":
			wheelPrice = 22
		elif self._comboBox3.Text == "58 mm":
			wheelPrice = 24
		elif self._comboBox3.Text == "61 mm":
			wheelPrice = 28
			
		if self._checkBox1.Checked:
			miscPrice = miscPrice + 10
		if self._checkBox2.Checked:
			miscPrice = miscPrice + 30
		if self._checkBox3.Checked:
			miscPrice = miscPrice + 2
		if self._checkBox4.Checked:
			miscPrice = miscPrice + 3
		if self._checkBox5.Checked:
			miscPrice = miscPrice + 10
		
		price = + wheelPrice + truckPrice + deckPrice + miscPrice
		tax = price * 0.06
		totalPrice = price * tax
		self._label5.Text = str(price)
		self._label7.Text = str(tax)
		