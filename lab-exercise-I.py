{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Adekunle Oliver Adebajo\n",
    "### 20120612016\n",
    "### adekunle.adebajo@pau.edu.ng\n",
    "### the following codes consist of class exercises involving problem solving"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "26\n",
      "7\n"
     ]
    }
   ],
   "source": [
    "def difference(n):\n",
    "    if n <= 17:\n",
    "        return 17 - n\n",
    "    else:\n",
    "        return (n - 17) * 2 \n",
    "\n",
    "print(difference(30))\n",
    "print(difference(10))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12\n",
      "45\n"
     ]
    }
   ],
   "source": [
    "def sum_thrice(x, y, z):\n",
    " \n",
    "     sum = x + y + z\n",
    " \n",
    "     if x == y == z:\n",
    "      sum = sum * 3\n",
    "     return sum\n",
    " \n",
    "print(sum_thrice(3, 4, 5))\n",
    "print(sum_thrice(5, 5, 5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "def test_number5(x, y):\n",
    "    if x == y or abs(x-y) == 5 or (x+y) == 5:\n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "\n",
    "print(test_number5(10, 5))\n",
    "print(test_number5(3, 4))\n",
    "print(test_number5(2, 3))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-22-30a5df4de358>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-22-30a5df4de358>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    if (a > c)\u001b[0m\n\u001b[1;37m              ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "if (a > c)\n",
    "   swap(a, c);\n",
    "\n",
    "if (a > b)\n",
    "   swap(a, b);\n",
    "\n",
    "//Now the smallest element is the 1st one. Just check the 2nd and 3rd\n",
    "\n",
    "if (b > c)\n",
    "   swap(b, c);\n",
    "    (a, b, c) == (2, 5, 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def sum_of_cubes(n):\n",
    "  n = 5\n",
    "  total = 0\n",
    "  while n > 0:\n",
    "    total += n * n * n\n",
    "    n = 5\n",
    "  return total\n",
    "print(\"Sum of cubes: \",sum_of_cubes(3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
