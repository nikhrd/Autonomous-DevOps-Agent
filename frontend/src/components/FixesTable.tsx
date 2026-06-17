interface Props {
  fixes: any[];
}

export default function FixesTable({
  fixes
}: Props) {

  return (
    <table
      className="w-full border"
    >
      <thead>
        <tr>
          <th>File</th>

          <th>Bug</th>

          <th>Line</th>

          <th>Status</th>
        </tr>
      </thead>

      <tbody>

        {fixes?.map(
          (
            fix,
            index
          ) => (
            <tr key={index}>

              <td>
                {fix.file}
              </td>

              <td>
                {fix.bug_type}
              </td>

              <td>
                {fix.line}
              </td>

              <td>
                {fix.status}
              </td>

            </tr>
          )
        )}

      </tbody>
    </table>
  );
}