import pandas as pd
from smartsheet import smartsheet


def get_sheet(token: str, sheet_id: int) -> pd.DataFrame:
    """
    Download SmartSheet and create pandas.DataFrame.

    Parameters
    ----------
    token : str
        SmartSheet API token
    sheet_id : int
        SmartSheet sheet identifier

    Returns
    -------
    pandas.DataFrame
        The requested SmartSheet as a DataFrame
    """
    sheet = smartsheet.Smartsheet(access_token=token).Sheets.get_sheet(
        sheet_id=sheet_id,
        include=["discussions", "rowPermalink", "writerInfo"],
    )
    return pd.DataFrame(
        data=[
            [sheet.id, row.id, row.permalink] + [cell.value for cell in row.cells]
            for row in sheet.rows
        ],
        columns=["sheet_id", "row_id", "permalink"]
        + [col.title for col in sheet.columns],
    )


def create_comment(token: str, sheet_id: int, row_id: int, comment_text: str) -> None:
    """
    Create a comment on a specified row of a SmartSheet.

    Parameters
    ----------
    token : str
        SmartSheet API token
    sheet_id : int
        SmartSheet sheet identifier
    row_id : int
        SmartSheet row identifier
    comment_text : str
        The text to comment
    """
    smartsheet_client = smartsheet.Smartsheet(token)
    smartsheet_client.Discussions.create_discussion_on_row(
        sheet_id,
        row_id,
        smartsheet.models.Discussion({
            "comment": smartsheet.models.Comment({"text": comment_text}),
        }),
    )


def build_update_rows(rows: dict[int, dict[int, str]]) -> list[smartsheet.models.Row]:
    update: list[smartsheet.models.Row] = []

    for row_id, cells in rows.items():
        new_row = smartsheet.models.Row()
        new_row.id = row_id

        for (
            column_id,
            value,
        ) in cells.items():
            new_cell = smartsheet.models.Cell()
            new_cell.column_id = column_id
            new_cell.value = value
            new_cell.strict = False
            new_row.cells.append(new_cell)

        update.append(new_row)
    return update


def update_rows(
    token: str,
    sheet_id: int,
    rows: list[smartsheet.models.Row],
) -> None:
    """
    Update rows in a smartsheet.

    Parameters
    ----------
    token : str
        SmartSheet API token
    sheet_id : int
        SmartSheet sheet identifier
    rows : list
        List of rows to update
    """
    smartsheet_client = smartsheet.Smartsheet(token)
    smartsheet_client.Sheets.update_rows(sheet_id=sheet_id, list_of_rows=rows)
