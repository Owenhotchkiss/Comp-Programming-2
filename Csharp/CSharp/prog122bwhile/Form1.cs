namespace prog122bwhile
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            listBox1.Items.Add("Hours\t\tPay");
            int lcv = 1;
            while (lcv <= 40)
            {
                int pay = lcv * 4;
                listBox1.Items.Add(lcv + "\t\t" + pay);
                lcv++;
            }
        }
    }
}