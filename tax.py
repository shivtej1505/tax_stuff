# --- Earnings --- #
basic = 0 + 0
hr_allowance = 0 + 0
conv_allowance = 0
med_allowance = 0
spc_allowance = 0 + 0
lt_allowance = 0 + 0
bonus = 0 + 0
dearness_allowance = 0
#lta = 0

# --- Expenses --- #
rent_paid = (8000*12) # Rent paid
#rent_paid = 4000 + 8000*10

total_salary = basic + hr_allowance + conv_allowance + med_allowance + spc_allowance + lt_allowance + bonus

def sprint(*args):
    pstr = ' '.join([str(a) for a in args])
    print(pstr)

sprint("Total Salary is:", total_salary)

###############################
# Exemptions Under Section 10 #
###############################

# --- HRA Tax Calculation --- #
hra1 = hr_allowance # Actual HRA received
hra2 = rent_paid - 0.1*(basic + dearness_allowance) # Rent paid minus(-) 10% of Basic + DA
hra3 = 0.4 * (basic + dearness_allowance) # 40 % of Basic + DA. Non-Metro Cities = 40%, Metro - 50%

exempt_hra = min(hra1, hra2, hra3)
sprint("Exempt HRA is:", exempt_hra)


# --- Conveyance Allowance Tax Calculation --- #
exempt_ca = min(conv_allowance, 1600*12)
#sprint("Exempt CA is:", exempt_ca)

# --- Medical Reimbursement --- #
# Medical Allowance and Medical Reimbursement are different.

med_reimb = 0

###############################
# Deductions Under Section 16 #
###############################
std_dedu = 40000 # Standard Deduction
pro_tax = 2300 # 2300


###############################
# Deductions Under 80C #
###############################
ppf = 150000
#elss = 0
#mutual_funds = 0
#med_insurance_dep = 0
#med_insurance_self = 0

###############################
# Deductions Under Section 80CCD(0B) #
###############################
nps = 50000 # National Pension Scheme
#nps = 0

#total_exemption = exempt_hra + exempt_ca
total_exemption = exempt_hra + + ppf + nps + std_dedu + pro_tax
#total_reimb = med_reimb

sprint("Total Exemption:", total_exemption)
#sprint("Total Reimbursement:", total_reimb)

total_taxable_income = total_salary - total_exemption
sprint("Total Taxable Income:", total_taxable_income)

if total_taxable_income <= 1000000:
    tax_percentage = 0.2
    fixed = 12500
    slab = 500000
else:
    tax_percentage = 0.3
    fixed = 112500
    slab = 1000000

tax_before_cess = (total_taxable_income - slab)*tax_percentage + fixed
sprint("Tax before cess:", tax_before_cess)

total_tax = 1.04*tax_before_cess
sprint("Total Tax before:", total_tax)



