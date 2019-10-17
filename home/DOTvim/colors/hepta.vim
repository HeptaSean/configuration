" hepta colors for vim
set background=dark
hi clear
if exists("syntax_on")
    syntax reset
endif
let g:colors_name="hepta"
" normal text
hi Normal gui=NONE guifg=#939393 guibg=#000000
        \ term=NONE cterm=NONE ctermfg=7 ctermbg=NONE
" the character under the cursor
hi Cursor gui=reverse guifg=#B7B7B7 guibg=NONE
        \ term=reverse cterm=reverse ctermfg=15 ctermbg=NONE
hi lCursor gui=NONE guifg=#B7B7B7 guibg=NONE
         \ term=NONE cterm=NONE ctermfg=15 ctermbg=NONE
" the screen column that the cursor is in when 'cursorcolumn' is set
hi CursorColumn gui=NONE guifg=NONE guibg=#484848
              \ term=NONE cterm=NONE ctermfg=NONE ctermbg=8
" the screen line that the cursor is in when 'cursorline' is set
hi clear CursorLine
hi link CursorLine CursorColumn
" used for the columns set with 'colorcolumn'
hi clear ColorColumn
hi link ColorColumn CursorColumn
" line used for closed folds
hi Folded gui=NONE guifg=#4BB7B7 guibg=#484848
        \ term=NONE cterm=NONE ctermfg=6 ctermbg=8
" 'foldcolumn'
hi clear FoldColumn
hi link FoldColumn Folded
" '~' and '@' at the end of the window
hi NonText gui=NONE guifg=#6F6FDB guibg=#484848
         \ term=NONE cterm=NONE ctermfg=4 ctermbg=8
hi NonTextBold gui=bold guifg=#9393FF guibg=#484848
             \ term=bold cterm=bold ctermfg=12 ctermbg=8
" Line number for ":number" and ":#" commands
hi clear LineNr
hi link LineNr NonText
hi clear CursorLineNr
hi link CursorLineNr NonTextBold
" tab pages line, not active tab page label
hi clear TabLine
hi link TabLine NonText
" tab pages line, active tab page label
hi TabLineSel gui=bold guifg=#9393FF guibg=NONE
            \ term=bold cterm=bold ctermfg=12 ctermbg=NONE
" tab pages line, where there are no labels
hi clear TabLineFill
hi link TabLineFill NonText
" column where |signs| are displayed
hi clear SignColumn
hi link SignColumn NonText
" status line of current window
hi clear StatusLine
hi link StatusLine NonTextBold
" status lines of not-current windows
hi clear StatusLineNC
hi link StatusLineNC NonText
" the column separating vertically split windows
hi clear VertSplit
hi link VertSplit NonText
" error messages on the command line
hi ErrorMsg gui=reverse,bold guifg=#FF9393 guibg=NONE
          \ term=reverse,bold cterm=reverse,bold ctermfg=9 ctermbg=NONE
" warning messages
hi WarningMsg gui=reverse guifg=#DB6F6F guibg=NONE
            \ term=reverse cterm=reverse ctermfg=1 ctermbg=NONE
" 'showmode' message (e.g., "-- INSERT --")
hi ModeMsg gui=reverse guifg=#6F6FDB guibg=NONE
         \ term=reverse cterm=reverse ctermfg=4 ctermbg=NONE
" |more-prompt|
hi clear MoreMsg
hi link MoreMsg ModeMsg
" |hit-enter| prompt and yes/no questions
hi Question gui=reverse,bold guifg=#93FF93 guibg=NONE
          \ term=reverse,bold cterm=reverse,bold ctermfg=10 ctermbg=NONE
" current match in 'wildmenu' completion
hi WildMenu gui=reverse,bold guifg=#DBDB6F guibg=NONE
          \ term=reverse,bold cterm=reverse,bold ctermfg=11 ctermbg=NONE
" popup menu: normal item
hi Pmenu gui=NONE guifg=#939393 guibg=#484848
       \ term=NONE cterm=NONE ctermfg=7 ctermbg=8
" popup menu: selected item
hi PmenuSel gui=reverse guifg=#6F6FDB guibg=NONE
          \ term=reverse cterm=reverse ctermfg=4 ctermbg=NONE
" popup menu: scrollbar
hi PmenuSbar gui=NONE guifg=#6F6FDB guibg=#484848
           \ term=NONE cterm=NONE ctermfg=4 ctermbg=8
" popup menu: thumb of the scrollbar
hi clear PmenuThumb
hi link PmenuThumb PmenuSbar
" visual mode selection
hi Visual gui=reverse guifg=#6F6FDB guibg=NONE
        \ term=reverse cterm=reverse ctermfg=4 ctermbg=NONE
" visual mode selection when vim is "Not Owning the Selection"
hi clear VisualNOS
hi link VisualNOS Visual
" diff mode: Deleted line |diff.txt|
hi DiffDelete gui=reverse guifg=#DB6F6F guibg=NONE
            \ term=reverse cterm=reverse ctermfg=1 ctermbg=NONE
" diff mode: Added line |diff.txt|
hi DiffAdd gui=reverse guifg=#6FDB6F guibg=NONE
         \ term=reverse cterm=reverse ctermfg=2 ctermbg=NONE
" diff mode: Changed text within a changed line |diff.txt|
hi DiffText gui=reverse guifg=#B7B74B guibg=NONE
          \ term=reverse cterm=reverse ctermfg=3 ctermbg=NONE
" diff mode: Changed line |diff.txt|
hi clear DiffChange
hi link DiffChange CursorColumn
" last search pattern highlighting (see 'hlsearch')
hi Search gui=reverse,bold guifg=#DBDB6F guibg=NONE
        \ term=reverse,bold cterm=reverse,bold ctermfg=11 ctermbg=NONE
" 'incsearch' highlighting
hi clear IncSearch
hi link IncSearch Search
" word that is not recognized
hi SpellBad gui=underline guifg=#DB6F6F guibg=NONE guisp=#DB6F6F
          \ term=underline cterm=underline ctermfg=1 ctermbg=NONE
" word that should start with a capital
hi SpellCap gui=underline guifg=#6F6FDB guibg=NONE guisp=#6F6FDB
          \ term=underline cterm=underline ctermfg=4 ctermbg=NONE
" word that is recognized as one that is hardly ever used
hi SpellRare gui=underline guifg=#B74BB7 guibg=NONE guisp=#B74BB7
           \ term=underline cterm=underline ctermfg=5 ctermbg=NONE
" word that is recognized as one that is used in another region
hi SpellLocal gui=underline guifg=#4BB7B7 guibg=NONE guisp=#4BB7B7
            \ term=underline cterm=underline ctermfg=6 ctermbg=NONE
" character, if it is a paired bracket, and its match
hi MatchParen gui=reverse guifg=#9393FF guibg=NONE
            \ term=reverse cterm=reverse ctermfg=12 ctermbg=NONE
" meta and special keys listed with ":map"
hi SpecialKey gui=NONE guifg=#4BB7B7 guibg=NONE
            \ term=NONE cterm=NONE ctermfg=6 ctermbg=NONE
" titles for output from ":set all", ":autocmd" etc.
hi Title gui=bold guifg=#9393FF guibg=NONE
       \ term=bold cterm=bold ctermfg=12 ctermbg=NONE
" directory names (and other special names in listings)
hi Directory gui=bold guifg=#9393FF guibg=NONE
           \ term=bold cterm=bold ctermfg=12 ctermbg=NONE
" place holder characters substituted for concealed text ('conceallevel')
hi Conceal gui=NONE guifg=#484848 guibg=NONE
         \ term=NONE cterm=NONE ctermfg=8 ctermbg=NONE
" highlight groups for syntax highlighting,
" just change foreground colours:
hi Comment gui=NONE guifg=#B7B74B guibg=NONE
         \ term=NONE cterm=NONE ctermfg=3 ctermbg=NONE
hi Constant gui=NONE guifg=#6FDB6F guibg=NONE
          \ term=NONE cterm=NONE ctermfg=2 ctermbg=NONE
hi clear Special
hi link Special SpecialKey
hi Identifier gui=NONE guifg=#B74BB7 guibg=NONE
            \ term=NONE cterm=NONE ctermfg=5 ctermbg=NONE
hi Statement gui=NONE guifg=#6F6FDB guibg=NONE
           \ term=NONE cterm=NONE ctermfg=4 ctermbg=NONE
hi clear PreProc
hi link PreProc Statement
hi clear Type
hi link Type Statement
hi Error gui=reverse,bold guifg=#FF9393 guibg=NONE
       \ term=reverse,bold cterm=reverse,bold ctermfg=9 ctermbg=NONE
hi Todo gui=reverse,bold guifg=#DBDB6F guibg=NONE
      \ term=reverse,bold cterm=reverse,bold ctermfg=11 ctermbg=NONE
hi Underlined gui=underline guifg=NONE guibg=NONE
            \ term=underline cterm=underline ctermfg=NONE ctermbg=NONE
"hi Ignore
