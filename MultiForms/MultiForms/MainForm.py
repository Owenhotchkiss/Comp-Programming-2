import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkCyan
		self._button1.FlatStyle = System.Windows.Forms.FlatStyle.Popup
		self._button1.ForeColor = System.Drawing.Color.Transparent
		self._button1.Location = System.Drawing.Point(90, 36)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(335, 216)
		self._button1.TabIndex = 0
		self._button1.Text = "Show New Form"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkOrange
		self.ClientSize = System.Drawing.Size(523, 315)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "MultiForms"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		from Form1 import *
		form1 = Form1(self, "Hello, World!")
		form1.Show()
		self.Hide()
		
#		from SecondForm import *
#		form2 = SecondForm
#		form2.Show()