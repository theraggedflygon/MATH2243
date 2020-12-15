const det = (matrix) => {
  const m = matrix.length;
  const n = matrix[0].length;

  // check to see if the matrix is square
  if (m !== n) {
    return null;
  }

  // if matrix is 2x2, return the determinant
  if (m === 2) {
    return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1];
  }

  let det_total = 0;
  det_list = [];
  Array.from(Array(m).keys()).map((i) => {
    let submat = JSON.parse(JSON.stringify(matrix)).splice(1);
    submat.map((r) => r.splice(i, 1));
    sub_det = det(submat);
    det_total += sub_det * matrix[0][i] * (-1) ** i;
  });

  return det_total;
};

if (require.main === module) {
  m2 = [
    [2, 4],
    [3, 1],
  ];

  m3 = [
    [1, 4, 5],
    [6, 7, 8],
    [9, 12, 4],
  ];

  big_matrix = [
    [10, 3, 9, 7, 10, 9, 8, 9, 3, 3],
    [5, 10, 5, 4, 3, 4, 10, 7, 8, 7],
    [2, 9, 7, 2, 4, 10, 10, 9, 3, 8],
    [8, 4, 6, 1, 4, 3, 8, 10, 6, 4],
    [5, 4, 7, 7, 5, 8, 5, 9, 4, 7],
    [10, 10, 4, 8, 4, 3, 6, 6, 2, 2],
    [5, 5, 8, 7, 3, 7, 7, 8, 5, 9],
    [4, 9, 6, 9, 4, 4, 9, 6, 7, 9],
    [4, 2, 6, 10, 3, 1, 3, 3, 1, 6],
    [3, 3, 4, 5, 5, 10, 2, 8, 10, 1],
  ];

  test_matrix = [
    [1, 4, 3, 4],
    [9, 8, 7, 6],
    [5, 4, 3, 2],
    [5, 7, 9, 10],
  ];

  start_time = Date.now();

  console.log(det(big_matrix));

  console.log(Date.now() - start_time);
}
