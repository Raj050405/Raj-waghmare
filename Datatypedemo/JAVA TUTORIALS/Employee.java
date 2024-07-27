public class Employee{
	String name, address;
	int empId, age;
	long contactno;
	String EmpDepartment;
	int Salary;

	int Salary_withdrawn(int amount)
	{
		return amount;
	}
	public static void main(String a[])
	{
		Employee Emp=new Employee();
		System.out.println("Emp salary withdrawn  "+ Emp.Salary_withdrawn(5000));
	}
}