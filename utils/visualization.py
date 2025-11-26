def render_state_html(state, tile_size=70):
    html = f"""
    <style>
    .grid {{
        display: inline-grid;
        grid-template-columns: repeat(3, {tile_size}px);
        gap: 8px;
    }}
    .tile {{
        width: {tile_size}px;
        height: {tile_size}px;
        display: flex;
        justify-content: center;
        align-items: center;
        background: #e0e0e0;
        border-radius: 12px;
        font-size: {tile_size*0.45}px;
        font-weight: 700;
        border: 2px solid #444;
    }}
    .blank {{
        background: #888;
    }}
    </style>
    <div class='grid'>
    """

    for n in state:
        if n == 0:
            html += "<div class='tile blank'></div>"
        else:
            html += f"<div class='tile'>{n}</div>"

    html += "</div>"
    return html
