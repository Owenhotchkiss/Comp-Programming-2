
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class frmGeneral(Form):
	def __init__(self, parent):
		self.myparent = parent
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.DodgerBlue
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.White
		self._textBox1.Location = System.Drawing.Point(195, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(228, 31)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.LightSkyBlue
		self._textBox2.Location = System.Drawing.Point(323, 90)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 1
		self._textBox2.TextChanged += self.TextBox2TextChanged
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.LightSkyBlue
		self._textBox3.Location = System.Drawing.Point(323, 136)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 2
		# 
		# textBox4
		# 
		self._textBox4.BackColor = System.Drawing.Color.LightSkyBlue
		self._textBox4.Location = System.Drawing.Point(323, 203)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(100, 20)
		self._textBox4.TabIndex = 3
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label2.Location = System.Drawing.Point(195, 139)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 5
		self._label2.Text = "Tax:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label3.Location = System.Drawing.Point(195, 199)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 6
		self._label3.Text = "Total:"
		self._label3.Click += self.Label3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label1.Location = System.Drawing.Point(195, 87)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 7
		self._label1.Text = "Price per Ticket:"
		# 
		# radioButton1
		# 
		self._radioButton1.BackColor = System.Drawing.Color.LightCoral
		self._radioButton1.Location = System.Drawing.Point(12, 81)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(104, 24)
		self._radioButton1.TabIndex = 8
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Section A"
		self._radioButton1.UseVisualStyleBackColor = False
		# 
		# radioButton2
		# 
		self._radioButton2.BackColor = System.Drawing.Color.LightCoral
		self._radioButton2.Location = System.Drawing.Point(12, 139)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(104, 24)
		self._radioButton2.TabIndex = 9
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Section B"
		self._radioButton2.UseVisualStyleBackColor = False
		# 
		# radioButton3
		# 
		self._radioButton3.BackColor = System.Drawing.Color.LightCoral
		self._radioButton3.Location = System.Drawing.Point(12, 199)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(104, 24)
		self._radioButton3.TabIndex = 10
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Section C"
		self._radioButton3.UseVisualStyleBackColor = False
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Gray
		self._button1.Location = System.Drawing.Point(12, 243)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(201, 77)
		self._button1.TabIndex = 12
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Gray
		self._button2.Location = System.Drawing.Point(222, 243)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(201, 77)
		self._button2.TabIndex = 13
		self._button2.Text = "Close"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.YellowGreen
		self._label4.Location = System.Drawing.Point(12, 12)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(158, 31)
		self._label4.TabIndex = 14
		self._label4.Text = "Number of Tickets:"
		# 
		# frmGeneral
		# 
		self.BackColor = System.Drawing.Color.LemonChiffon
		self.ClientSize = System.Drawing.Size(435, 332)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._radioButton3)
		self.Controls.Add(self._radioButton2)
		self.Controls.Add(self._radioButton1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "frmGeneral"
		self.Text = "frmGeneral"
		self.ResumeLayout(False)
		self.PerformLayout()


	def TextBox2TextChanged(self, sender, e):
		pass

	def Label3Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		numTickets = int(self._textBox1.Text)
		ppt = 0
		tax = 0.06
		if self._radioButton1.Checked:
			ppt = 20
		elif self._radioButton2.Checked:
			ppt = 15
		elif self._radioButton3.Checked:
			ppt = 10
		total = numTickets * tax * ppt
		self._textBox2.Text = str(ppt)
		self._textBox3.Text = str(tax)
		self._textBox4.Text = str(total)

	def Button2Click(self, sender, e):
		Application.Exit()