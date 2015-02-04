#include<iostream>
#include<cstdlib>

using namespace std;

int main()
{
	int size = 4;

	char board[size][size];
	int row_val[size], col_val[size];

	int result = 0;		//1 : Player 1, -1: Player 2 win

	int i, j,dg1=0,dg2=0;

	system("clear");

	for(i = 0; i<size; ++i)
	{
		for(j =0; j<size; ++j)
		{

			board[i][j] = ' ';
			cout<<"["<<board[i][j]<<"]\t";
		}
		cout<<endl;
	}

	for(i = 0; i<size; ++i)
	{
		row_val[i] = 0;
		col_val[i] = 0;
	}

	int row, col;

	for(int k = 1; k<=(size*size)/2 + 1; k++)
	{
		re1:
		cout<<"\nPlayer 1 enter row and columns \n";
		cin>>row>>col;

		if(row>size || row<1 || col>size || col<1 || board[row-1][col-1]!=' ')
		{
			cout<<"Invalid choice";
			goto re1;
		}

		board[row-1][col-1] = 'O';
		row_val[row-1]++;
		col_val[col-1]++;

		if(row==col)
			dg1++;
		if(row+col==size)
			dg2++;

		if(row_val[row-1]==size || col_val[col-1]==size || dg1==size || dg2==size)
			result=1;




		system("clear");

		for(i = 0; i<size; ++i)
		{
			cout<<endl;
			for(j = 0; j<size; ++j)
				cout<<"["<<board[i][j]<<"]\t";
		}

		if(result==1)
		{
			cout<<"Player 1 wins"<<endl;
			break;
		}

		if(k == size*size/2 + 1)
			break;


		re2:
		cout<<"\nPlayer 2 enter row and columns \n";
		cin>>row>>col;

		if(row>size || row<1 || col>size || col<1 || board[row-1][col-1]!=' ')
		{
			cout<<"Invalid choice";
			goto re2;
		}

		board[row-1][col-1] = 'X';

		row_val[row-1]--;
		col_val[col-1]--;

		if(row==col)
			dg1--;
		if(row+col==size+1)
			dg2--;

		if(row_val[row-1]==-size || col_val[col-1]==-size || dg1==-size || dg2==-size)
			result=-1;

		system("clear");

		for(i = 0; i<size; ++i)
		{
			cout<<endl;
			for(j  = 0; j<size; ++j)
				cout<<"["<<board[i][j]<<"]\t";
		}

		if(result==-1)
		{
			cout<<"Player 2 wins"<<endl;
			break;
		}

	}

	if(result == 0)
		cout<<"DRAW"<<endl;

	return 0;

}

