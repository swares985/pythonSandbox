from decimal import Decimal

a = Decimal('1.1');
b = Decimal('4.55');
decimalResult = a ** b;

f1 = float(1.1);
f2 = float(4.55);
floatResult = f1 ** f2;

print('Python lets us use Decimal math, which is arbitrary precision.');
print('This is different from floating point math, as we\'ll show below.\n\n');

print('The result of float math: {0:03.75f}'.format(floatResult));
print('The result of Decimal math: {0:03.75f}\n'.format(decimalResult));

floatConversion = Decimal(floatResult);
epsilon = decimalResult - floatConversion;
absEpsilon = epsilon.copy_abs();

print('The difference between these two is: {0:.60f}'.format(absEpsilon));
print('Seem like a small deal?');
print('Well, what if we, say, are projecting this epsilon as occurring 100 times a second,');
print('of every minute, of every hour, of every day, for 10 years? (That\'s 315360000 seconds,');
print('by the way.');
print('');
print('We\'d realize the error is now significant...');

tenYearsOfSeconds = Decimal('3156000000');
tenYearsOfErrors = tenYearsOfSeconds * absEpsilon;

print('Mathematically, you now have an error (epsilon) of:\nEpsilon: {0:.75f}'.format(tenYearsOfErrors));
print('That\'s an error percentage of:')

percentageError = tenYearsOfErrors / decimalResult;

print('Error: {0:.30%}'.format(percentageError));
