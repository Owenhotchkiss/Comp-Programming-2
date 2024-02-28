
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class fromStudent(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkOrchid
		self._label1.Location = System.Drawing.Point(12, 27)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Number of Tickets:"
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Thistle
		self._textBox1.Location = System.Drawing.Point(118, 30)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 1
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.HotPink
		self._label2.Location = System.Drawing.Point(12, 113)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 2
		self._label2.Text = "Tickets:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.HotPink
		self._label4.Location = System.Drawing.Point(12, 150)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 4
		self._label4.Text = "Tax:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.HotPink
		self._label6.Location = System.Drawing.Point(12, 188)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 6
		self._label6.Text = "Total:"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.CornflowerBlue
		self._button1.Location = System.Drawing.Point(12, 244)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(114, 61)
		self._button1.TabIndex = 8
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.CornflowerBlue
		self._button2.Location = System.Drawing.Point(132, 244)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(124, 61)
		self._button2.TabIndex = 9
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = False
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.Thistle
		self._textBox2.Location = System.Drawing.Point(118, 150)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 10
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.Thistle
		self._textBox3.Location = System.Drawing.Point(118, 191)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 11
		# 
		# textBox4
		# 
		self._textBox4.BackColor = System.Drawing.Color.Thistle
		self._textBox4.Location = System.Drawing.Point(118, 113)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(100, 20)
		self._textBox4.TabIndex = 12
		# 
		# fromStudent
		# 
		self.BackColor = System.Drawing.Color.SlateBlue
		self.ClientSize = System.Drawing.Size(291, 317)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "fromStudent"
		self.Text = "fromStudent"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		numTickets = int(self._textBox1.Text)
		price = 7
		cost = numTickets * price
		tax = 0.06
		total = cost * 0.06
		self._textBox4.Text = str(cost)
		self._textBox2.Text = str(tax)
		self._textBox3.Text = str(total)
		