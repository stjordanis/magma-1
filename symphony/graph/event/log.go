// Copyright (c) 2004-present Facebook All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package event

import (
	"context"

	"github.com/facebookincubator/symphony/pkg/ent"
	"github.com/facebookincubator/symphony/pkg/event"
)

func (e *Eventer) logHook() ent.Hook {
	return event.LogHook(func(ctx context.Context, entry event.LogEntry) error {
		e.emit(ctx, event.EntMutation, entry)
		return nil
	}, e.Logger)
}
