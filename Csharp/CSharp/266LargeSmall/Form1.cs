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
            int Bignum = 0;

            if (num1 > num2);
            Bignum = num1;
            if (num2 > num1);
            Bignum = num2;
            else;
            textBox3.Text = "The numbers given are equal";
        }
    }
}
