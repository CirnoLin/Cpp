#include<iostream>
#include<string>
using namespace std;

int main() {
	int bai, shi, yi, temp;
	string num, a, b, c, d;
	cin >> num;
	a = num.erase(1, 1);
	b = num.erase(0, 1);
	c = num.erase(1, 1);
	d = num.erase(0, 2);
	bai = a[0];
	shi = c[0];
	yi = d[0];
	while (bai > 0) {
		cout << "B";
		bai--;
	}
	while (shi > 0) {
		cout << "S";
		shi--;
	}
	cout << yi << endl;
	return 0;
}
