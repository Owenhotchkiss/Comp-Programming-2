import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.IndianRed
		self._label1.Location = System.Drawing.Point(12, 35)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Number 1"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.IndianRed
		self._label2.Location = System.Drawing.Point(12, 68)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Number 2"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.IndianRed
		self._label3.Location = System.Drawing.Point(12, 104)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Number 3"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.IndianRed
		self._label4.Location = System.Drawing.Point(12, 134)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 3
		self._label4.Text = "Number 4"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.IndianRed
		self._label5.Location = System.Drawing.Point(12, 231)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 4
		self._label5.Text = "Sum:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.IndianRed
		self._label6.Location = System.Drawing.Point(12, 272)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 5
		self._label6.Text = "Average:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(119, 35)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 6
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(119, 70)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 7
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(119, 104)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 8
		# 
		# textBox4
		# 
		self._textBox4.Location = System.Drawing.Point(119, 136)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(100, 20)
		self._textBox4.TabIndex = 9
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(268, 215)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(89, 47)
		self._button1.TabIndex = 10
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(363, 213)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(90, 49)
		self._button2.TabIndex = 11
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(268, 268)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(185, 45)
		self._button3.TabIndex = 12
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Tan
		self._label7.Location = System.Drawing.Point(141, 231)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 13
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Tan
		self._label8.Location = System.Drawing.Point(141, 268)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 14
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Coral
		self.ClientSize = System.Drawing.Size(465, 317)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "prog54b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		num3 = int(self._textBox3.Text)
		num4 = int(self._textBox4.Text)
		Sum1 = num1 + num2 + num3 + num4
		average = Sum1 / 4.0
		self._label7.Text = str(Sum1)
		self._label8.Text = str(average)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._textBox4.Text = ""
		self._label7.Text = ""
		self._label8.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()