def pascal_triangle(n):
    # Check if n is less than or equal to 0
    if n <= 0:
        return []  # Return an empty list if n is invalid
    
    triangle = [[1]]  # Initialize the triangle with the first row containing a single 1
    
    # Generate the subsequent rows of the triangle
    for i in range(1, n):
        row = [1]  # Start each row with a 1
        
        # Calculate each element of the current row
        for j in range(1, i):
            # Each element is the sum of the corresponding elements from the previous row
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        
        row.append(1)  # End each row with a 1
        triangle.append(row)  # Append the current row to the triangle
    
    return triangle  # Return the completed triangle
