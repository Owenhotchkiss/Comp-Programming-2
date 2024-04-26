using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace _266LargeSmall
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            int num1 = int.Parse(textBox1.Text);
            int num2 = int.Parse(textBox2.Text);

            if (num1 > num2)
            {
                textBox3.Text = num1.ToString();
            } else if (num2 > num1)
            {
                textBox3.Text = num2.ToString();
            } else
            {
                textBox3.Text = "The numbers given are equal";
            }
            
        }
    }
}
